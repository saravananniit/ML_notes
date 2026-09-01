# Multiclass Classification: Predicting Student Grade (Single Class Output from Multiple Classes)

## Use Case

Predict a student's grade based on study hours.

Possible Classes:

- A Grade = 0
- B Grade = 1
- C Grade = 2

This is called **Multiclass Classification** because the output can be one class from more than two classes.

---

# Step 1: Dataset

| Student | Study Hours (X) | Grade (Y) |
|----------|----------------|-----------|
| 1 | 1 | C (2) |
| 2 | 2 | C (2) |
| 3 | 3 | B (1) |
| 4 | 4 | B (1) |
| 5 | 5 | A (0) |
| 6 | 6 | A (0) |

Number of Records:

n = 6

---

# Step 2: Why Binary Classification Cannot Be Used

Binary Classification predicts only:

- 0 or 1

Examples:

- Pass / Fail
- Spam / Not Spam

Here we have:

- A
- B
- C

Three classes.

Therefore, we use:

## Multiclass Logistic Regression (Softmax Regression)

---

# Step 3: Softmax Formula

First calculate score for each class.

For each class:

z = β₀ + β₁X

Assume after training we get:

### Class A

zA = -10 + 3X

### Class B

zB = -2 + 1X

### Class C

zC = 5 - 1X

---

# Step 4: Convert Scores into Probabilities

Softmax Formula:

P(Class i) = e^zi / Σe^z

Properties:

- All probabilities are between 0 and 1
- Sum of probabilities = 1

---

# Step 5: Prediction Example

Suppose:

Study Hours = 4

---

## Calculate Scores

### Class A

zA = -10 + 3(4)

zA = 2

---

### Class B

zB = -2 + 1(4)

zB = 2

---

### Class C

zC = 5 - 1(4)

zC = 1

---

# Step 6: Calculate Exponential Values

e² = 7.389

e² = 7.389

e¹ = 2.718

Total:

7.389 + 7.389 + 2.718

= 17.496

---

# Step 7: Calculate Probabilities

## Class A

P(A)

= 7.389 / 17.496

= 0.422

= 42.2%

---

## Class B

P(B)

= 7.389 / 17.496

= 0.422

= 42.2%

---

## Class C

P(C)

= 2.718 / 17.496

= 0.156

= 15.6%

---

# Step 8: Select Highest Probability

| Class | Probability |
|---------|------------|
| A | 42.2% |
| B | 42.2% |
| C | 15.6% |

Highest Probability:

42.2%

Predicted Class:

A or B

(In practice the model chooses the slightly higher probability.)

---

# Step 9: Predict All Records

Assume model predictions are:

| Actual Grade | Predicted Grade |
|-------------|-----------------|
| C | C |
| C | C |
| B | B |
| B | B |
| A | A |
| A | B |

---

# Step 10: Confusion Matrix

| Actual \ Predicted | A | B | C |
|-------------------|---|---|---|
| A | 1 | 1 | 0 |
| B | 0 | 2 | 0 |
| C | 0 | 0 | 2 |

---

# Step 11: Calculate Accuracy

Formula:

Accuracy

= Correct Predictions / Total Predictions

Calculation:

Accuracy

= (1 + 2 + 2) / 6

= 5 / 6

= 0.833

= 83.3%

---

# Step 12: Calculate Precision

For Class A:

Precision(A)

= TP / (TP + FP)

= 1 / (1 + 0)

= 1

= 100%

---

For Class B:

Precision(B)

= 2 / (2 + 1)

= 0.667

= 66.7%

---

For Class C:

Precision(C)

= 2 / (2 + 0)

= 1

= 100%

---

# Step 13: Calculate Recall

For Class A:

Recall(A)

= 1 / (1 + 1)

= 0.5

= 50%

---

For Class B:

Recall(B)

= 2 / (2 + 0)

= 100%

---

For Class C:

Recall(C)

= 2 / (2 + 0)

= 100%

---

# Step 14: Calculate F1 Score

Formula:

F1

= 2 × Precision × Recall

  / (Precision + Recall)

Example for Class A:

F1

= 2 × 1 × 0.5

  / (1 + 0.5)

= 0.667

= 66.7%

---

# Step 15: Train-Test Split

Typical Split:

- 70% Train + 30% Test
- 80% Train + 20% Test

Purpose:

- Train on historical data.
- Evaluate on unseen data.

---

# Step 16: Predict a New Student

Suppose:

Study Hours = 7

Scores:

zA = -10 + 3(7) = 11

zB = -2 + 1(7) = 5

zC = 5 - 1(7) = -2

After Softmax:

| Grade | Probability |
|---------|-------------|
| A | 99% |
| B | 1% |
| C | 0% |

Prediction:

Grade A

---

# Final Summary

## Model Type

Multiclass Classification

---

## Number of Classes

3

- A Grade
- B Grade
- C Grade

---

## Evaluation Metrics

| Metric | Value |
|----------|--------|
| Accuracy | 83.3% |
| Precision | Per Class |
| Recall | Per Class |
| F1 Score | Per Class |

---

## New Prediction

| Study Hours | Predicted Grade |
|-------------|----------------|
| 7 | A |

---

# One-Liner

Multiclass Classification predicts one class from more than two possible classes.

General Formula (Softmax):

P(Class i) = e^zi / Σe^z

Examples:

- Student Grade → A, B, C
- Animal → Cat, Dog, Horse
- News Category → Sports, Politics, Business
- Digit Recognition → 0 to 9

---

# Quick Comparison

## Simple Linear Regression

Input → 1 Feature

Output → Continuous Value

Example:

Experience → Salary

---

## Multiple Linear Regression

Input → Multiple Features

Output → Continuous Value

Example:

Experience + Education → Salary

---

## Binary Classification

Input → One or More Features

Output → 2 Classes

Example:

Study Hours → Pass/Fail

---

## Multiclass Classification

Input → One or More Features

Output → More Than 2 Classes

Example:

Study Hours → Grade A/B/C