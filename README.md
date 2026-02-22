# Customer Segmentation System 

An end-to-end machine learning system that segments customers using RFM analysis and KMeans clustering, enhanced with Isolation Forest for detecting anomalous customer behavior within each segment.



## Overview

• Built a complete customer segmentation pipeline using RFM features  
• Applied KMeans clustering to group customers based on behavior  
• Integrated Isolation Forest for anomaly detection within clusters  
• Designed for real-world business use cases (marketing & customer insights)  
• Deployed as an interactive system with API + frontend  



## Objectives

• Segment customers into meaningful behavioral groups  
• Detect unusual or risky customer patterns within clusters  
• Identify high-value, low-engagement, and anomalous users  
• Enable data-driven decision-making  
• Build a production-ready ML system  



## What Was Done

• Performed RFM (Recency, Frequency, Monetary) analysis  
• Scaled features for clustering consistency  
• Trained KMeans model for segmentation  

• Performed anomaly detection using Isolation Forest:
  - Applied model on RFM features  
  - Detected outliers based on isolation mechanism  
  - Flagged customers with unusual behavior patterns  
  - Analyzed anomalies within each cluster  

• Built FastAPI backend for prediction  
• Developed Streamlit UI for user interaction  
• Deployed using Docker on Render  



## Model Details

• Clustering Algorithm: KMeans  
• Anomaly Detection: Isolation Forest  
• Type: Unsupervised Learning  

• Input Features:
  - Recency (days since last purchase)
  - Frequency (transaction count)
  - Monetary (total spend)

• Output:
  - Customer Segment (e.g., Potential Loyalists, etc.)
  - Anomaly Flag (Normal / Anomalous — from analysis phase)



## System Architecture

• Model Layer → KMeans + Isolation Forest (trained in notebook)  
• FastAPI → Handles prediction requests (`/predict`)  
• Streamlit → UI for entering RFM values  
• Deployment → Docker-based deployment on Render  



## Key Highlights

• End-to-end ML system (Model + API + UI)  
• Real-time segmentation via deployed API  
• Isolation Forest adds strong anomaly detection capability  
• Cluster-wise anomaly insights improve business understanding  
• Efficient deployment using Docker  



## Example

Input:  
Recency = 10  
Frequency = 1  
Monetary = 500  

Output:  
→ Segment: Potential Loyalists   



## Conclusion

• Demonstrates strong understanding of unsupervised learning  
• Combines clustering + anomaly detection effectively  
• Focuses on both analytics and system design  
• Suitable for real-world customer analytics applications
