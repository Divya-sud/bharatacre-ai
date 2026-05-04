import pickle

def predict_future():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    future = model.make_future_dataframe(periods=1825)
    forecast = model.predict(future)

    result = forecast[['ds', 'yhat']].tail(5)

    return result.to_dict(orient='records')