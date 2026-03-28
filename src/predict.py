import pandas as pd

def predict(model, screen_time, unlocks, notifications):
    data = pd.DataFrame([[screen_time, unlocks, notifications]],
                        columns=["screen_time", "unlocks", "notifications"])

    prediction = model.predict(data)[0]

    if prediction == 2:
        return "High"
    elif prediction == 1:
        return "Medium"
    else:
        return "Low"