from fastapi import FastAPI
from app.predictor import predict_customer
from app.schema import Customer

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/predict")
def predict(customer: Customer):
    return predict_customer(customer.dict())


