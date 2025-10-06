# Homework 02 – Regression

This project is part of the **ML Engineering Zoomcamp** by **DataTalks Club**.  
The goal of this homework was to implement a **linear regression model from scratch** to predict **car fuel efficiency (MPG)** using numerical vehicle features.

---

## 🧩 What I Did

I began by loading the dataset `car_fuel_efficiency.csv` and selecting only the relevant numerical columns:

- `engine_displacement`
- `horsepower`
- `vehicle_weight`
- `model_year`
- `fuel_efficiency_mpg` (target variable)

After exploring the dataset, I discovered that the **`horsepower`** column contained missing values (708 out of 9704 rows).  
I visualized the target variable (`fuel_efficiency_mpg`) and found that it followed a roughly **bell-shaped distribution**.

---

## ⚙️ Handling Missing Values

I compared two approaches for handling missing values in the `horsepower` column:

1. Filling missing values with `0`
2. Filling missing values with the **mean** of the column

After training and evaluating both versions of the model, I found that the mean imputation strategy performed better, giving a lower RMSE.

---

## 🧠 Model Implementation

I implemented **linear regression manually** using the **normal equation**:

\[
w = (X^T X)^{-1} X^T y
\]

Steps included:
- Adding a bias column (intercept term)
- Writing a function for prediction
- Creating a reusable RMSE evaluation function

I also implemented **ridge regularization (L2)** and tested multiple values of the regularization parameter `r`.  
However, RMSE remained stable across all tested values, indicating regularization had little effect in this dataset.

---

## 📊 Model Evaluation and Stability

To test model stability, I repeated the training/validation split 10 times with different random seeds.  
The RMSE values were nearly identical across runs, with a **standard deviation of 0.008** — confirming model consistency.

Finally, I retrained the model using the combined training and validation data and evaluated it on the **test set**.

---

## 🧩 What I Learned

- How to implement linear regression **from scratch** using matrix operations  
- How to handle **missing data** and evaluate different strategies  
- The purpose of **regularization** and how it influences model complexity  
- How to assess **model stability** across random seeds  
- The importance of **data preparation** before model training  

---

## 🧰 Tools and Libraries

- **Python**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **scikit-learn**

---

## Final Thoughts

This homework improved my understanding of the inner workings of linear regression.  
Building everything manually helped me appreciate the math and logic behind `scikit-learn`’s implementation.  

---

