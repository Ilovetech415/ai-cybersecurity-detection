from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np
from sklearn.ensemble import IsolationForest
from utils.feature_engineering import extract_features
import logging

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("security-ai")

# Train model (simulated data)
model = IsolationForest(contamination=0.1)
X_train = np.random.rand(200, 3)
model.fit(X_train)

class LoginAttempt(BaseModel):
    failed_attempts: int
    time_interval: float
    ip_requests: int

@app.get("/")
def home():
    return {"status": "Cybersecurity AI Detection Running"}

@app.post("/detect-login")
def detect_login(attempts: List[LoginAttempt]):
    features = [extract_features(a.dict()) for a in attempts]
    X = np.array(features)

    preds = model.predict(X)

    results = []
    for i, p in enumerate(preds):
        if p == -1:
            logger.warning(f"Suspicious activity detected: {attempts[i]}")
            results.append("⚠️ Suspicious Activity")
        else:
            results.append("✅ Normal")

    return {"analysis": results}
