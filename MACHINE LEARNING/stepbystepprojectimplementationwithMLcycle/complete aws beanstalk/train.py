import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

# Load dataset
df = pd.read_csv("Algerian_forest_fires_dataset.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove null rows
df.dropna(inplace=True)

# Encode Classes column
df['Classes'] = df['Classes'].str.strip()

df['Classes'] = df['Classes'].map({
    'not fire': 0,
    'fire': 1
})

# Encode Region
if 'Region' in df.columns:
    df['Region'] = pd.factorize(df['Region'])[0]

# Convert columns to numeric
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.dropna(inplace=True)

# Features and target
X = df.drop('FWI', axis=1)
y = df['FWI']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

# Train Ridge
ridge = Ridge(alpha=1.0)

ridge.fit(X_train, y_train)

# Save model
pickle.dump(ridge, open('ridge.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("Model Saved Successfully")