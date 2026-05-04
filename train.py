import pandas as pd
from prophet import Prophet
import pickle

df = pd.read_csv("data/sample_data.csv")

model = Prophet()
model.fit(df)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully")