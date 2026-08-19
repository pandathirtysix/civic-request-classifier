from datasets import load_dataset
import pandas as pd

# Load dataset
ds = load_dataset("JadeSamLee/civicdex")

# Convert train split to pandas
data = ds["train"].to_pandas()


# Save as CSV
data.to_csv("datasets/dataset/data.csv", index=False)

