# Binary Classification: Predicting Pass or Fail (Single Value Output)

## Use Case

Predict whether a student will:

- 0 = Fail
- 1 = Pass

based on a single input feature:

- X = Study Hours

This is called **Binary Classification** because the output can take only one of two values.

---

# Step 1: Dataset

| Student | X (Study Hours) | Y (Pass/Fail) |
|----------|----------------|---------------|
| 1 | 1 | 0 |
| 2 | 2 | 0 |
| 3 | 3 | 0 |
| 4 | 4 | 1 |
| 5 | 5 | 1 |

Where:

- 0 = Fail
- 1 = Pass

Number of records:

n = 5

---

# Step 2: Why Linear Regression Cannot Be Used

Suppose Linear Regression predicts:

ŷ = 1.8

or

ŷ = -0.5

But classification requires only:

- 0 (Fail)
- 1 (Pass)

Therefore we use **Logistic Regression**.

---

# Step 3: Logistic Regression Formula

Instead of a straight line, Logistic Regression uses a Sigmoid Function.

Formula:

p = 1 / (1 + e^-(β₀ + β₁X))

Where:

- p = Probability of Passing
- β₀ = Intercept
- β₁ = Coefficient
- X = Study Hours

Output range:

0 ≤ p ≤ 1

---

# Step 4: Assume Calculated Coefficients

After training, assume:

β₀ = -7

β₁ = 2

---

# Step 5: Build Classification Equation

Substitute values:

p = 1 / (1 + e^-(-7 + 2X))

This is the trained model.

---

# Step 6: Calculate Probabilities

## Student 1

X = 1

z = -7 + 2(1)

z = -5

p = 1/(1+e^5)

p = 1/(1+148.41)

p = 0.0067

Prediction:

Fail (0)

---

## Student 2

X = 2

z = -7 + 2(2)

z = -3

p = 1/(1+e^3)

p = 0.0474

Prediction:

Fail (0)

---

## Student 3

X = 3

z = -7 + 2(3)

z = -1

p = 1/(1+e^1)

p = 0.2689

Prediction:

Fail (0)

---

## Student 4

X = 4

z = -7 + 2(4)

z = 1

p = 1/(1+e^-1)

p = 0.7311

Prediction:

Pass (1)

---

## Student 5

X = 5

z = -7 + 2(5)

z = 3

p = 1/(1+e^-3)

p = 0.9526

Prediction:

Pass (1)

---

# Step 7: Apply Decision Threshold

Classification Rule:

If p ≥ 0.5

Predict = 1 (Pass)

Else

Predict = 0 (Fail)

---

# Step 8: Predicted Results

| X | Actual Y | Probability (p) | Predicted Y |
|---|---|---|---|
| 1 | 0 | 0.0067 | 0 |
| 2 | 0 | 0.0474 | 0 |
| 3 | 0 | 0.2689 | 0 |
| 4 | 1 | 0.7311 | 1 |
| 5 | 1 | 0.9526 | 1 |

---

# Step 9: Confusion Matrix

| Actual \ Predicted | Fail (0) | Pass (1) |
|-------------------|-----------|-----------|
| Fail (0) | 3 | 0 |
| Pass (1) | 0 | 2 |

---

# Step 10: Calculate Accuracy

Formula:

Accuracy = Correct Predictions / Total Predictions

Calculation:

Accuracy = (3 + 2) / 5

Accuracy = 5/5

Accuracy = 1.0

Accuracy = 100%

---

# Step 11: Precision

Formula:

Precision = TP / (TP + FP)

Calculation:

Precision = 2 / (2 + 0)

Precision = 1

Precision = 100%

---

# Step 12: Recall

Formula:

Recall = TP / (TP + FN)

Calculation:

Recall = 2 / (2 + 0)

Recall = 1

Recall = 100%

---

# Step 13: F1 Score

Formula:

F1 = 2 × (Precision × Recall) / (Precision + Recall)

Calculation:

F1 = 2 × (1 × 1) / (1 + 1)

F1 = 1

F1 = 100%

---

# Step 14: Train-Test Split

Typical Split:

- 70% Train + 30% Test
- 80% Train + 20% Test

Purpose:

- Train using historical data.
- Validate using unseen data.

---

# Step 15: Predict New Student

Suppose:

Study Hours = 6

## Calculate z

z = -7 + 2(6)

z = 5

---

## Calculate Probability

p = 1/(1+e^-5)

p = 0.9933

---

## Classification

p = 0.9933 > 0.5

Prediction = 1

Result = Pass

---

# Final Summary

## Learned Logistic Equation

p = 1/(1 + e^-(-7 + 2X))

---

## Evaluation Metrics

| Metric | Value |
|----------|--------|
| Accuracy | 100% |
| Precision | 100% |
| Recall | 100% |
| F1 Score | 100% |

---

## New Prediction

| Study Hours | Probability | Predicted Class |
|-------------|-------------|----------------|
| 6 | 0.9933 | Pass (1) |

---

# One-Liner

Binary Classification predicts one of two possible classes (0 or 1, Yes or No, Pass or Fail) using input features.

### Logistic Regression Formula

p = 1 / (1 + e^-(β₀ + β₁X))

### Decision Rule

- If Probability ≥ 0.5 → Class 1
- If Probability < 0.5 → Class 0

### Examples

- Pass / Fail
- Spam / Not Spam
- Fraud / Genuine Transaction
- Customer Churn / No Churn
- Disease / No Disease

---

# Quick Comparison

### Simple Linear Regression

- Input: 1 Feature
- Output: 1 Continuous Value
- Example: Experience → Salary

### Multiple Linear Regression

- Input: Multiple Features
- Output: 1 Continuous Value
- Example: Experience + Education → Salary

### Binary Classification

- Input: One or More Features
- Output: One Class (0 or 1)
- Example: Study Hours → Pass/Fail