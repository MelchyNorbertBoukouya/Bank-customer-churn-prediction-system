
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
from database import SessionLocal, Prediction

app = FastAPI(
    title="Bank Customer Churn Prediction API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load trained model
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
model_columns = joblib.load("models/model_columns.pkl")


class Customer(BaseModel):
    credit_score: int
    geography: str
    gender: str
    age: int
    tenure: int
    balance: float
    num_products: int
    has_credit_card: int
    is_active_member: int
    estimated_salary: float


@app.get("/")
def home():
    return {
        "message": "Bank Churn Prediction API is running"
    }

@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame({
        "CreditScore": [customer.credit_score],
        "Geography": [customer.geography],
        "Gender": [customer.gender],
        "Age": [customer.age],
        "Tenure": [customer.tenure],
        "Balance": [customer.balance],
        "NumOfProducts": [customer.num_products],
        "HasCrCard": [customer.has_credit_card],
        "IsActiveMember": [customer.is_active_member],
        "EstimatedSalary": [customer.estimated_salary]
    })

    # Encoding
    data = pd.get_dummies(
        data,
        columns=["Geography", "Gender"],
        drop_first=True
    )

    # Match training columns
    data = data.reindex(
        columns=model_columns,
        fill_value=0
    )

    # Scaling
    data_scaled = scaler.transform(data)

    # Prediction
    prediction = model.predict(data_scaled)[0]

    probability = model.predict_proba(
        data_scaled
    )[0][1]

    # Risk level
    if probability >= 0.70:
        risk = "High"

    elif probability >= 0.40:
        risk = "Medium"

    else:
        risk = "Low"


    # ==========================
    # SAVE TO DATABASE
    # ==========================

    db = SessionLocal()

    new_prediction = Prediction(

        credit_score=customer.credit_score,
        geography=customer.geography,
        gender=customer.gender,
        age=customer.age,
        tenure=customer.tenure,

        balance=customer.balance,
        num_products=customer.num_products,

        has_credit_card=customer.has_credit_card,
        is_active_member=customer.is_active_member,

        estimated_salary=customer.estimated_salary,

        prediction=int(prediction),

        churn_probability=float(probability),

        churn_percentage=float(probability * 100),

        risk_level=risk
    )

    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    db.close()


    return {

        "prediction": int(prediction),

        "churn_probability":
            round(float(probability), 4),

        "churn_percentage":
            round(float(probability * 100), 2),

        "risk_level":
            risk,

        "prediction_id":
            new_prediction.id
    }
