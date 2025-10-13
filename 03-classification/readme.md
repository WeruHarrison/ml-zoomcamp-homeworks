# Homework 03 – Classification

This repo contains my solution and reflection for **Module 3 – Classification**.  
The task: build a simple classification pipeline from scratch (and with `scikit-learn`) to predict whether a lead converts, using a toy dataset of course leads.

---

## What I worked on

I implemented a classification workflow using `pandas`, `NumPy`, and `scikit-learn`.  
Main steps: data cleaning, feature engineering (one-hot encoding), model training with logistic regression, feature importance checks (via mutual information and leave-one-out accuracy), and hyperparameter tuning for regularization strength. The goal was to practise classification basics and the full ML workflow.

---

## What I learned

- Simple features can be the most predictive for conversion in this dataset — quality > quantity of features.
- Mutual information helped me quickly identify which categorical variables might be useful
- Hyperparameter tuning for logistic regression (regularization) matters less when the predictive signal is strong and the dataset is small.
- Practicing the full pipeline (clean → encode → train → validate → tune)

---

## Tools Used

Python
Pandas
NumPy
Matplotlib
Seaborn
scikit-learn

---

## Final Thoughts
This homework deepened my understanding of classification and feature analysis. Working through the questions helped me appreciate the importance of preprocessing and evaluating feature contributions before modeling. It was a great step toward mastering practical machine learning workflows.