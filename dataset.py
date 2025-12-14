import pandas as pd
import numpy as np

np.random.seed(42)

n_per_class = 500

def make_block(churn_value):
    tenure = np.random.randint(1, 72, n_per_class)
    monthly = np.round(np.random.uniform(20, 120, n_per_class), 2)

    return pd.DataFrame({
        "gender": np.random.randint(0, 2, n_per_class),
        "SeniorCitizen": np.random.randint(0, 2, n_per_class),
        "Partner": np.random.randint(0, 2, n_per_class),
        "Dependents": np.random.randint(0, 2, n_per_class),
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": np.round(tenure * monthly, 2),
        "Churn": churn_value
    })

df = pd.concat([
    make_block(0),
    make_block(1)
], ignore_index=True)

# Shuffle rows
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv("churn_dataset_1k.csv", index=False)

print("Generated churn_dataset_1k.csv with shape:", df.shape)
print(df["Churn"].value_counts())
