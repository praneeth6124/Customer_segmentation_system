import joblib

from customer_pipeline import CustomerSegmentationPipeline


pipeline = joblib.load("model/customer_segmentation.pkl")

def predict_customer(data):
    return pipeline.predict(data)






