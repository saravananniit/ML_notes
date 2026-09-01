# Centroid Example in Detail (K-Means Clustering)

## Why is Centroid Important?

Centroid is one of the most important concepts in K-Means clustering.

A **centroid** is simply the **center point of a cluster**.

Think of it like this:

If 10 students are standing together in a group, the centroid is the position that best represents the **middle of the group**.

In K-Means clustering:

- Each cluster has one centroid.
- Every data point is assigned to the nearest centroid.
- Centroids keep moving until the clusters become stable.

---

# Customer Clustering Example

Suppose we have customer data with two features:

1. Age
2. Income

## Dataset

| Customer | Age | Income |
|----------|-----|--------|
| C1 | 20 | 40 |
| C2 | 22 | 45 |
| C3 | 24 | 50 |
| C4 | 50 | 90 |
| C5 | 52 | 95 |
| C6 | 55 | 100 |

---

## Visual Observation

Looking at the data:

### Group 1

- (20,40)
- (22,45)
- (24,50)

### Group 2

- (50,90)
- (52,95)
- (55,100)

These naturally form **two groups (clusters)**.

---

# Step 1: Calculate Centroids

A centroid is calculated by taking the average of all feature values within a cluster.

---

## Cluster A

### Age Average

```text
(20 + 22 + 24) / 3

= 66 / 3

= 22
```

### Income Average

```text
(40 + 45 + 50) / 3

= 135 / 3

= 45
```

### Centroid A

```text
(22, 45)
```

---

## Cluster B

### Age Average

```text
(50 + 52 + 55) / 3

= 157 / 3

= 52.33
```

### Income Average

```text
(90 + 95 + 100) / 3

= 285 / 3

= 95
```

### Centroid B

```text
(52.33, 95)
```

---

# Visual Representation

```text
Income

100 |                    * C6
 95 |                * C5
 90 |             * C4

 50 |      * C3
 45 |    * C2
 40 |  * C1
     ------------------------
      20 25      50 55 Age
```

### Approximate Centroids

```text
Cluster A Centroid = (22,45)

Cluster B Centroid = (52.33,95)
```

These points sit approximately at the center of their clusters.

---

# Step 2: New Customer Arrives

Suppose a new customer enters:

```text
Age    = 23
Income = 48
```

Point:

```text
(23,48)
```

Now K-Means asks:

> Which centroid is closer?

---

# Step 3: Distance to Cluster A

K-Means commonly uses **Euclidean Distance**.

## Formula

```text
Distance = √((x₁-c₁)² + (x₂-c₂)²)
```

Where:

- x = customer data point
- c = centroid

---

### Customer

```text
(23,48)
```

### Centroid A

```text
(22,45)
```

### Calculation

```text
DistanceA

= √((23-22)² + (48-45)²)

= √(1² + 3²)

= √(1 + 9)

= √10

= 3.16
```

---

# Step 4: Distance to Cluster B

### Centroid B

```text
(52.33,95)
```

### Calculation

```text
DistanceB

= √((23-52.33)² + (48-95)²)

= √((-29.33)² + (-47)²)

= √(860 + 2209)

= √3069

= 55.4
```

---

# Step 5: Compare Distances

```text
Distance to Cluster A = 3.16

Distance to Cluster B = 55.4
```

Since:

```text
3.16 < 55.4
```

the customer belongs to:

## ✅ Cluster A

The new customer is assigned to Cluster A because its centroid is much closer.

---

# Real-Life Analogy

Imagine there are two cities:

- Chennai
- Bangalore

You are standing somewhere between them.

To determine which city is closer:

1. Measure distance to Chennai.
2. Measure distance to Bangalore.
3. Choose the smaller distance.

K-Means works exactly the same way.

```text
Cities      → Centroids
Kilometers  → Feature Distance
```

Whichever centroid is nearest wins.

---

# Why Does K-Means Keep Updating Centroids?

Suppose Cluster A initially contains:

```text
(20,40)
(22,45)
(24,50)
```

Current centroid:

```text
(22,45)
```

Now a new customer joins:

```text
(25,52)
```

Cluster becomes:

```text
(20,40)
(22,45)
(24,50)
(25,52)
```

---

## Recalculate Centroid

### Age

```text
(20 + 22 + 24 + 25) / 4

= 91 / 4

= 22.75
```

### Income

```text
(40 + 45 + 50 + 52) / 4

= 187 / 4

= 46.75
```

### New Centroid

```text
(22.75, 46.75)
```

---

## What Happened?

The centroid moved from:

```text
(22,45)
```

to

```text
(22.75,46.75)
```

because the cluster gained a new member.

The center of the cluster changed.

---

# Complete K-Means Iteration Process

K-Means repeatedly performs the following steps:

## Step 1

Choose initial centroids.

## Step 2

Assign every point to its nearest centroid.

## Step 3

Recalculate centroids using cluster averages.

## Step 4

Check whether centroids moved.

### If moved:

Repeat Steps 2 and 3.

### If not moved:

Stop.

Clusters are now stable.

---

# K-Means Flow

```text
Initialize Centroids
          ↓
Calculate Distance
          ↓
Assign Points to Nearest Centroid
          ↓
Recalculate Centroids
          ↓
Centroids Changed?
      ↙         ↘
    Yes         No
     ↓           ↓
 Repeat      Stop
```

---

# Interview Question

## What is a centroid in K-Means clustering?

**Answer:**

A centroid is the center point of a cluster. It is calculated by taking the average value of all features of the records belonging to that cluster. During K-Means clustering, each record is assigned to the nearest centroid, and the centroids are repeatedly updated until the cluster assignments become stable.

---

# Easy Memory Tricks

### Regression

```text
Regression → Draw a Line
```

### Classification

```text
Classification → Choose a Class
```

### Clustering

```text
Clustering → Find Similar Groups
```

### Centroid

```text
Centroid → Center of a Group
```

---

# One-Line Definition

**Centroid is the average position of all data points belonging to a cluster and represents the center of that cluster.**

✅ Whenever you hear **Centroid**, think:

> "The average position of all records in that cluster."