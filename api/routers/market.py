from fastapi import APIRouter
from pydantic import BaseModel
from core.models.rf_survival import FirmExitPredictor
import random

router = APIRouter()
rf_predictor = FirmExitPredictor()

class FirmData(BaseModel):
    liquidity_ratio: float
    debt_to_equity: float
    employee_turnover: float
    market_demand_trend: float

@router.post("/predict-exit")
def predict_firm_exit(data: FirmData):
    """
    Predicts the socio-economic impact by calculating exit probability.
    """
    features = [
        data.liquidity_ratio,
        data.debt_to_equity,
        data.employee_turnover,
        data.market_demand_trend
    ]
    
    risk_prob = rf_predictor.predict_exit_probability(features)
    
    return {
        "status": "success",
        "exit_probability": risk_prob,
        "recommendation": "High risk of exit. Trigger government assistance protocols." if risk_prob > 0.7 else "Firm is currently stable."
    }

@router.get("/valuation/{node_id}")
def get_node_valuation(node_id: str):
    # This simulates ML models quantifying non-linear economic shocks 
    return {
        "node_id": node_id,
        "intangible_value_usd": random.randint(500000, 2000000),
        "stability_index": round(random.uniform(0.4, 0.9), 2),
        "patent_count": random.randint(1, 15),
        "risk_status": "Stable" if random.random() > 0.3 else "High Risk"
    }