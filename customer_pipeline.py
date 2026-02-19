

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


class CustomerSegmentationPipeline:

    def __init__(self):

        self.scaler = StandardScaler()

        self.kmeans = KMeans(
            n_clusters=4,
            random_state=42,
            n_init=20
        )

        self.features = ['Recency','Frequency','Monetary']

        # will be created AFTER fitting
        self.segment_map = {}


    def _build_segment_map(self, X_scaled):

        """
        Automatically assign segment names
        based on cluster statistics.
        """

    
        df = pd.DataFrame(X_scaled, columns=self.features)
        df['Cluster'] = self.kmeans.labels_

        profile = df.groupby('Cluster').mean()

        # Elite → high monetary + high frequency
        elite = profile.sort_values(
            ['Monetary','Frequency'],
            ascending=False
        ).index[0]

        # At risk → worst recency
        at_risk = profile.sort_values(
            ['Recency'],
            ascending=False
        ).index[0]

        # Loyal → next highest frequency (excluding elite)
        loyal = profile.drop(elite).sort_values(
            ['Frequency'],
            ascending=False
        ).index[0]

        # Remaining cluster
        remaining = list(set(profile.index) - {elite, loyal, at_risk})[0]

        self.segment_map = {
            elite: "Elite Customers",
            loyal: "Loyal Customers",
            remaining: "Potential Loyalists",
            at_risk: "At-Risk Customers"
        }


    def fit(self, X):

        X = X[self.features]

        X_log = np.log1p(X)

        X_scaled = self.scaler.fit_transform(X_log)

        self.kmeans.fit(X_scaled)


        self._build_segment_map(X_scaled)


    def predict(self, X):

        if not hasattr(self.scaler, "mean_"):
            raise RuntimeError("Model is not fitted yet.")

        if not self.segment_map:
            raise RuntimeError("Segment map not built. Fit the model first.")

        if not isinstance(X, dict):
            raise ValueError(
                "Input must be a dictionary with keys: Recency, Frequency, Monetary"
            )

        X = pd.DataFrame([X])[self.features]

        X_log = np.log1p(X)

        X_scaled = self.scaler.transform(X_log)

        cluster = self.kmeans.predict(X_scaled)[0]

        return {
            "segment": self.segment_map[cluster]
        }
