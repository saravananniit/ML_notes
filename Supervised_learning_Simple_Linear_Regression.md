# Simple Linear Regression: Predicting Salary from Years of Experience

## Use Case

Predict an employee's salary based on their years of experience.

- Input (X): Years of Experience
- Output (Y): Salary (in $1000s)

---

# Step 1: Dataset

| Employee | X (Years of Experience) | Y (Salary in $1000s) |
|----------|-------------------------|----------------------|
| 1 | 1 | 2 |
| 2 | 2 | 4 |
| 3 | 3 | 5 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |

Number of observations:

n = 5

---

# Step 2: Calculate Mean

## Mean of X

Formula:

x̄ = ΣX / n

Calculation:

x̄ = (1 + 2 + 3 + 4 + 5) / 5

x̄ = 15 / 5

x̄ = 3

---

## Mean of Y

Formula:

ȳ = ΣY / n

Calculation:

ȳ = (2 + 4 + 5 + 4 + 5) / 5

ȳ = 20 / 5

ȳ = 4

---

# Step 3: Calculate Slope (β₁)

## Formula

β₁ = Σ[(xᵢ - x̄)(yᵢ - ȳ)] / Σ[(xᵢ - x̄)²]

---

## Calculate Sxy

| X | Y | X - x̄ | Y - ȳ | (X - x̄)(Y - ȳ) |
|---|---|--------|--------|----------------|
| 1 | 2 | -2 | -2 | 4 |
| 2 | 4 | -1 | 0 | 0 |
| 3 | 5 | 0 | 1 | 0 |
| 4 | 4 | 1 | 0 | 0 |
| 5 | 5 | 2 | 1 | 2 |

Sxy = 4 + 0 + 0 + 0 + 2

Sxy = 6

---

## Calculate Sxx

| X | X - x̄ | (X - x̄)² |
|---|--------|----------|
| 1 | -2 | 4 |
| 2 | -1 | 1 |
| 3 | 0 | 0 |
| 4 | 1 | 1 |
| 5 | 2 | 4 |

Sxx = 4 + 1 + 0 + 1 + 4

Sxx = 10

---

## Calculate β₁

β₁ = Sxy / Sxx

β₁ = 6 / 10

β₁ = 0.6

Interpretation:

For every additional 1 year of experience, salary increases by 0.6 ($600).

---

# Step 4: Calculate Intercept (β₀)

## Formula

β₀ = ȳ - β₁x̄

## Calculation

β₀ = 4 - (0.6 × 3)

β₀ = 4 - 1.8

β₀ = 2.2

Interpretation:

When experience is 0 years, predicted salary is 2.2 ($2200).

---

# Step 5: Build Regression Equation

## Formula

ŷ = β₀ + β₁X

Substituting values:

ŷ = 2.2 + 0.6X

This is the trained model.

---

# Step 6: Predict Training Data

| X | Actual Y | Predicted Ŷ = 2.2 + 0.6X | Residual (Y - Ŷ) |
|---|----------|--------------------------|------------------|
| 1 | 2 | 2.8 | -0.8 |
| 2 | 4 | 3.4 | 0.6 |
| 3 | 5 | 4.0 | 1.0 |
| 4 | 4 | 4.6 | -0.6 |
| 5 | 5 | 5.2 | -0.2 |

Residual Sum:

-0.8 + 0.6 + 1.0 - 0.6 - 0.2 = 0

OLS Property:

Σe = 0 ✔

---

# Step 7: Calculate Error Metrics

## SSE (Sum of Squared Errors)

Formula:

SSE = Σ(Y - Ŷ)²

Calculation:

SSE = (-0.8)² + (0.6)² + (1.0)² + (-0.6)² + (-0.2)²

SSE = 0.64 + 0.36 + 1.00 + 0.36 + 0.04

SSE = 2.40

---

## MAE (Mean Absolute Error)

Formula:

MAE = Σ|Y - Ŷ| / n

Calculation:

MAE = (0.8 + 0.6 + 1.0 + 0.6 + 0.2) / 5

MAE = 3.2 / 5

MAE = 0.64

---

## MSE (Mean Squared Error)

Formula:

MSE = SSE / n

Calculation:

MSE = 2.4 / 5

MSE = 0.48

---

## RMSE (Root Mean Squared Error)

Formula:

RMSE = √MSE

Calculation:

RMSE = √0.48

RMSE = 0.6928

---

# Step 8: Calculate R² Score

## SST (Total Sum of Squares)

Formula:

SST = Σ(Y - ȳ)²

Calculation:

SST = (2-4)² + (4-4)² + (5-4)² + (4-4)² + (5-4)²

SST = 4 + 0 + 1 + 0 + 1

SST = 6

---

## R² Formula

R² = 1 - (SSE / SST)

Calculation:

R² = 1 - (2.4 / 6)

R² = 1 - 0.4

R² = 0.60

Interpretation:

The model explains 60% of the variation in salary.

---

# Step 9: Train-Test Split

Typical data split:

- 70% Training + 30% Testing
- 80% Training + 20% Testing

Purpose:

- Train the model using training data.
- Validate performance using unseen test data.

---

# Step 10: Predict New Data

Suppose a new employee has:

X = 6 years experience

Using:

ŷ = 2.2 + 0.6X

Calculation:

ŷ = 2.2 + (0.6 × 6)

ŷ = 2.2 + 3.6

ŷ = 5.8

### Predicted Salary

Salary = $5.8k

or

Salary = $5,800

---

# Final Summary

## Learned Equation

ŷ = 2.2 + 0.6X

## Metrics

| Metric | Value |
|----------|--------|
| MAE | 0.64 |
| MSE | 0.48 |
| RMSE | 0.6928 |
| R² | 0.60 |

## New Prediction

| Experience | Predicted Salary |
|------------|------------------|
| 6 Years | $5.8k |

---

# One-Liner

Simple Linear Regression uses one independent variable (X) to predict one continuous dependent variable (Y) by fitting the best straight-line equation:

ŷ = β₀ + β₁X

where:

- β₀ = Intercept
- β₁ = Slope
- ŷ = Predicted Value
- X = Input Feature