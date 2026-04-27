from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

# -----------------------------
# Load trained pipeline
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "churn_pipeline.pkl")

model = joblib.load(model_path)

# -----------------------------
# Input schema
# -----------------------------
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# -----------------------------
# Prediction Route
# -----------------------------
@app.post("/predict")
def predict(data: CustomerData):
    try:
        # Convert input to dataframe
        input_df = pd.DataFrame([data.model_dump()])

        # Predict
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        return {
            "churn_prediction": int(prediction),
            "churn_probability": float(probability)
        }

    except Exception as e:
        return {"error": str(e)}