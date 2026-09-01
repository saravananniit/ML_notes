"""
train_model.py
----------------
Trains a simple Linear Regression model using data from a CSV file
and saves the trained model as a .pkl file.

Expected CSV format (default: data.csv):
    years_experience,salary
    1,30000
    2,35000
    ...

The first column is the feature (X), the second column is the target (y).
Change FEATURE_COL / TARGET_COL below if your CSV uses different column names.
"""

import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# -----------------------------
# 1. Config
# -----------------------------
CSV_PATH = "data.csv"
FEATURE_COL = "years_experience"
TARGET_COL = "salary"
MODEL_PATH = "regression_model.pkl"

# -----------------------------
# 2. Load data from CSV
# -----------------------------
df = pd.read_csv(CSV_PATH)
print("Loaded data from:", CSV_PATH)
print(df.head())

X = df[[FEATURE_COL]]   # keep as DataFrame (2D) for sklearn
y = df[TARGET_COL]

# -----------------------------
# 3. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 4. Train the model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# 5. Evaluate on test split
# -----------------------------
y_pred = model.predict(X_test)
print("\nModel Coefficient (slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)
print("R2 Score on test data:", r2_score(y_test, y_pred))
print("MSE on test data:", mean_squared_error(y_test, y_pred))

# -----------------------------
# 6. Save model to a .pkl file
# -----------------------------
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"\nModel trained and saved to '{MODEL_PATH}'")

# -----------------------------
# 7. Optional: test immediately with a runtime user value
# -----------------------------
try:
    user_val = input(f"\nEnter a value for '{FEATURE_COL}' to test prediction now (or press Enter to skip): ").strip()
    if user_val:
        val = float(user_val)
        prediction = model.predict(pd.DataFrame([[val]], columns=[FEATURE_COL]))
        print(f"Predicted {TARGET_COL} for {FEATURE_COL}={val}: {prediction[0]:.2f}")
except Exception as e:
    print("Skipping runtime test:", e)
