import pandas as pd
import pickle

data_ = {
    "name": ["mr developer"],
    "street": ["udemy_"],
    "phone Num": ["67676767"],
    "raw_report" : ["test complient"],
    "intent": ["complaint"],
    "department": ["Transport Department"],
    "severity": ["medium"],
    "urgency": ["medium"],
    "category": ["transport"]
}

data = pd.DataFrame(data_)

with open(
    "datasets/reportsdata/database.pkl",
    "wb"
) as f:
    pickle.dump(data, f)



