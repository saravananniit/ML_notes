# Multiple Linear Regression: Predicting Salary from Experience and Education

## Use Case

Predict an employee's salary using multiple input features.

### Inputs (Features)

- X₁ = Years of Experience
- X₂ = Education Level (Years of Education)

### Output (Target)

- Y = Salary (in $1000s)

---

# Step 1: Dataset

| Employee | X₁ Experience | X₂ Education | Y Salary |
|----------|--------------|-------------|-----------|
| 1 | 1 | 12 | 25 |
| 2 | 2 | 14 | 32 |
| 3 | 3 | 15 | 38 |
| 4 | 4 | 16 | 44 |
| 5 | 5 | 18 | 52 |

Number of observations:

n = 5

---

# Step 2: Calculate Means

## Mean of X₁

Formula:

x̄₁ = ΣX₁ / n

Calculation:

x̄₁ = (1+2+3+4+5)/5

x̄₁ = 15/5

x̄₁ = 3

---

## Mean of X₂

Formula:

x̄₂ = ΣX₂ / n

Calculation:

x̄₂ = (12+14+15+16+18)/5

x̄₂ = 75/5

x̄₂ = 15

---

## Mean of Y

Formula:

ȳ = ΣY / n

Calculation:

ȳ = (25+32+38+44+52)/5

ȳ = 191/5

ȳ = 38.2

---

# Step 3: Build Multiple Regression Equation

Unlike Simple Linear Regression:

ŷ = β₀ + β₁X

Multiple Linear Regression uses:

ŷ = β₀ + β₁X₁ + β₂X₂

Where:

- β₀ = Intercept
- β₁ = Experience Coefficient
- β₂ = Education Coefficient

---

# Step 4: Calculate Coefficients

The coefficients are calculated using Matrix Formula:

β = (X'X)⁻¹X'Y

Where:

- X = Feature Matrix
- X' = Transpose of X
- Y = Target Vector

For real projects, Python, Excel, R, or SPSS performs this calculation automatically.

Assume the computed coefficients are:

β₀ = -5

β₁ = 4

β₂ = 2

---

# Step 5: Final Regression Equation

Substitute coefficients:

ŷ = -5 + 4X₁ + 2X₂

Interpretation:

- Every extra year of Experience increases Salary by 4 units.
- Every extra year of Education increases Salary by 2 units.

---

# Step 6: Predict Training Data

## Employee 1

X₁ = 1

X₂ = 12

ŷ = -5 + 4(1) + 2(12)

ŷ = -5 + 4 + 24

ŷ = 23

Residual:

e = 25 - 23 = 2

---

## Employee 2

X₁ = 2

X₂ = 14

ŷ = -5 + 4(2) + 2(14)

ŷ = -5 + 8 + 28

ŷ = 31

Residual:

e = 32 - 31 = 1

---

## Employee 3

X₁ = 3

X₂ = 15

ŷ = -5 + 4(3) + 2(15)

ŷ = -5 + 12 + 30

ŷ = 37

Residual:

e = 38 - 37 = 1

---

## Employee 4

X₁ = 4

X₂ = 16

ŷ = -5 + 4(4) + 2(16)

ŷ = -5 + 16 + 32

ŷ = 43

Residual:

e = 44 - 43 = 1

---

## Employee 5

X₁ = 5

X₂ = 18

ŷ = -5 + 4(5) + 2(18)

ŷ = -5 + 20 + 36

ŷ = 51

Residual:

e = 52 - 51 = 1

---

# Step 7: Calculate SSE

Formula:

SSE = Σ(Y - Ŷ)²

Calculation:

SSE = 2² + 1² + 1² + 1² + 1²

SSE = 4 + 1 + 1 + 1 + 1

SSE = 8

---

# Step 8: Calculate MAE

Formula:

MAE = Σ|Y - Ŷ| / n

Calculation:

MAE = (2+1+1+1+1)/5

MAE = 6/5

MAE = 1.2

---

# Step 9: Calculate MSE

Formula:

MSE = SSE / n

Calculation:

MSE = 8/5

MSE = 1.6

---

# Step 10: Calculate RMSE

Formula:

RMSE = √MSE

Calculation:

RMSE = √1.6

RMSE = 1.265

---

# Step 11: Calculate R²

## SST

Formula:

SST = Σ(Y - ȳ)²

Calculation:

SST

= (25-38.2)² + (32-38.2)² + (38-38.2)² + (44-38.2)² + (52-38.2)²

= 174.24 + 38.44 + 0.04 + 33.64 + 190.44

= 436.8

---

## R²

Formula:

R² = 1 - (SSE/SST)

Calculation:

R² = 1 - (8/436.8)

R² = 1 - 0.0183

R² = 0.9817

R² ≈ 98.17%

Interpretation:

The model explains approximately 98% of salary variation.

---

# Step 12: Train-Test Split

Typical splits:

- 70% Train + 30% Test
- 80% Train + 20% Test

Purpose:

- Train on historical data.
- Test on unseen data.

---

# Step 13: Predict New Employee

Suppose:

Experience = 6 years

Education = 17 years

Using:

ŷ = -5 + 4X₁ + 2X₂

Calculation:

ŷ = -5 + 4(6) + 2(17)

ŷ = -5 + 24 + 34

ŷ = 53

### Predicted Salary

Salary = $53k

---

# Final Summary

## Learned Equation

ŷ = -5 + 4X₁ + 2X₂

Where:

- X₁ = Experience
- X₂ = Education

---

## Metrics

| Metric | Value |
|----------|----------|
| SSE | 8 |
| MAE | 1.2 |
| MSE | 1.6 |
| RMSE | 1.265 |
| R² | 98.17% |

---

## New Prediction

| Experience | Education | Predicted Salary |
|------------|------------|------------------|
| 6 Years | 17 Years | $53k |

---

# One-Liner

Multiple Linear Regression uses two or more independent variables (X₁, X₂, X₃, ...) to predict one continuous dependent variable (Y).

General Formula:

ŷ = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ

Examples:

- House Price = Area + Bedrooms + Age
- Salary = Experience + Education
- Ice Cream Sales = Temperature + Rainfall + Holiday


Key Difference from Simple Linear Regression

Simple Linear Regression → 1 Input → 1 Output

Salary = Experience

Multiple Linear Regression → Multiple Inputs → 1 Output

Salary = Experience + Education
House Price = Area + Bedrooms + Age

This is usually the next topic taught after Simple Linear Regression.