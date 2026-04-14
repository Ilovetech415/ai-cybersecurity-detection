from fastapi import FastAPI
import numpy as np
from sklearn.ensemble import IsolationForest

app = FastAPI()

# Train a simple model
model = IsolationForest(contamination=0.1)
X_train = np.random.rand(100, 3)
model.fit(X_train)

@app.get("/")
def home():
    return {"message": "Cybersecurity AI Detection Running"}

@app.post("/detect")
def detect(data: list):
    X = np.array(data)
    preds = model.predict(X)
    results = ["Normal" if p == 1 else "Anomaly" for p in preds]
    return {"results": results}
