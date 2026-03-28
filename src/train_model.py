import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def train_model():
    data = {
        "screen_time": [1,2,3,4,5,6,7,8],
        "unlocks": [10,20,30,40,50,60,70,80],
        "notifications": [20,30,40,50,60,70,80,90],
        "label": ["Low","Low","Medium","Medium","Medium","High","High","High"]
    }

    df = pd.DataFrame(data)

    X = df[["screen_time","unlocks","notifications"]]
    y = df["label"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    return model