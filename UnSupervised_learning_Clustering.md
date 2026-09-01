

# Unsupervised Learning: Clustering Using K-Means

## Use Case

A retail company wants to group customers based on their spending habits.

There is no target column.

We only have customer information.

Objective:

Find similar customers and automatically group them into clusters.

This is called **Clustering**.

---

# Step 1: Dataset

| Customer | Monthly Spending ($1000) |
|-----------|-------------------------|
| C1 | 2 |
| C2 | 3 |
| C3 | 4 |
| C4 | 10 |
| C5 | 11 |
| C6 | 12 |

Number of records:

n = 6

Goal:

Create K = 2 clusters.

---

# Step 2: Choose Number of Clusters

K = 2

Meaning:

We want the algorithm to create 2 groups.

Example:

Cluster 1 = Low-spending customers

Cluster 2 = High-spending customers

---

# Step 3: Select Initial Centroids

Choose two initial centroids.

Suppose:

Centroid 1 = 2

Centroid 2 = 10

Notation:

μ₁ = 2

μ₂ = 10

---

# Step 4: Calculate Distance from Each Centroid

Distance Formula:

Distance = | Data Point - Centroid |

---

## Customer C1

Value = 2

Distance from μ₁

= |2 - 2|

= 0

Distance from μ₂

= |2 - 10|

= 8

Assigned Cluster:

Cluster 1

---

## Customer C2

Value = 3

Distance from μ₁

= |3 - 2|

= 1

Distance from μ₂

= |3 - 10|

= 7

Assigned Cluster:

Cluster 1

---

## Customer C3

Value = 4

Distance from μ₁

= |4 - 2|

= 2

Distance from μ₂

= |4 - 10|

= 6

Assigned Cluster:

Cluster 1

---

## Customer C4

Value = 10

Distance from μ₁

= |10 - 2|

= 8

Distance from μ₂

= |10 - 10|

= 0

Assigned Cluster:

Cluster 2

---

## Customer C5

Value = 11

Distance from μ₁

= |11 - 2|

= 9

Distance from μ₂

= |11 - 10|

= 1

Assigned Cluster:

Cluster 2

---

## Customer C6

Value = 12

Distance from μ₁

= |12 - 2|

= 10

Distance from μ₂

= |12 - 10|

= 2

Assigned Cluster:

Cluster 2

---

# Step 5: First Cluster Assignment

| Customer | Spending | Cluster |
|-----------|----------|----------|
| C1 | 2 | C1 |
| C2 | 3 | C1 |
| C3 | 4 | C1 |
| C4 | 10 | C2 |
| C5 | 11 | C2 |
| C6 | 12 | C2 |

---

# Step 6: Recalculate Centroids

## Cluster 1

Values:

2, 3, 4

Formula:

Centroid = Sum of Values / Number of Values

Calculation:

μ₁

= (2 + 3 + 4) / 3

= 9 / 3

= 3

---

## Cluster 2

Values:

10, 11, 12

Calculation:

μ₂

= (10 + 11 + 12) / 3

= 33 / 3

= 11

---

# Step 7: New Centroids

Old Centroids:

μ₁ = 2

μ₂ = 10

New Centroids:

μ₁ = 3

μ₂ = 11

---

# Step 8: Repeat Assignment

Calculate distances again.

For all customers, the cluster assignment remains the same.

No customer changes cluster.

Therefore:

Algorithm Converged.

Training Stops.

---

# Step 9: Final Clusters

## Cluster 1

Low-Spending Customers

{2, 3, 4}

Centroid = 3

---

## Cluster 2

High-Spending Customers

{10, 11, 12}

Centroid = 11

---

# Step 10: Calculate WCSS

WCSS = Within Cluster Sum of Squares

Formula:

WCSS = Σ(Data Point - Centroid)²

---

## Cluster 1

Centroid = 3

(2-3)² + (3-3)² + (4-3)²

= 1 + 0 + 1

= 2

---

## Cluster 2

Centroid = 11

(10-11)² + (11-11)² + (12-11)²

= 1 + 0 + 1

= 2

---

## Total WCSS

WCSS

= 2 + 2

= 4

Smaller WCSS indicates better clustering.

---

# Step 11: Predict a New Customer

Suppose:

Monthly Spending = 13

Distance from Cluster 1 Centroid

= |13 - 3|

= 10

Distance from Cluster 2 Centroid

= |13 - 11|

= 2

Since 2 is smaller,

Customer belongs to:

Cluster 2

(High-Spending Group)

---

# Step 12: Choosing Optimal K (Elbow Method)

Try different K values.

| K | WCSS |
|---|---|
| 1 | 80 |
| 2 | 4 |
| 3 | 2 |
| 4 | 1 |

Plot:

K vs WCSS

Choose the point where reduction starts slowing down.

This point is called the:

Elbow Point

Optimal K.

---

# Final Summary

## Algorithm

K-Means Clustering

---

## Input

Customer Spending

---

## Output

Cluster Membership

---

## Final Clusters

Cluster 1

Low Spending Customers

{2,3,4}

Centroid = 3

---

Cluster 2

High Spending Customers

{10,11,12}

Centroid = 11

---

## Evaluation Metric

WCSS = 4

Lower is Better.

---

## New Prediction

Customer Spending = 13

Assigned Cluster = Cluster 2

---

# One-Liner

K-Means Clustering is an Unsupervised Learning algorithm that groups similar data points into K clusters by repeatedly assigning points to the nearest centroid and recalculating centroids until convergence.

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

Input → Features

Output → Pass / Fail

---

## Multiclass Classification

Input → Features

Output → A / B / C

---

## Clustering (Unsupervised Learning)

Input → Features Only

Output → Groups / Clusters

Example:

Customers → Low Spenders / High Spenders


Next logical topic after Clustering:

Hierarchical Clustering
Association Rule Mining (Market Basket Analysis - Apriori)
Dimensionality Reduction (PCA)
Anomaly Detection

These are the most common Unsupervised Learning algorithms taught after K-Means.