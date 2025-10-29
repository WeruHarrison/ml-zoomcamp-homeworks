# Homework 04 – Evaluation

This repo contains my solution and reflection for **Module 4 – Evaluation** of the Machine Learning Zoomcamp by Datatalks Club led by Alexey Grigorev.
Tne goal of the homework was to practice evaluation of logistic regression models using
* Confusion Table
* Precision & Recall
* F1 Score
* ROC Curve and ROC AUC Scores
* Cross Validation
The model I used was for predicting whether a lead in a course platform can be converted to subscriber or not. 
---

## 🧰 Tools & Library
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
---

## 🧩 What I Did
I began creating the model using the `course_lead_scoring.csv` dataset. The model was already developed in an earlier [homework](https://github.com/WeruHarrison/ml-zoomcamp-homeworks/tree/main/03-classification). 
1. I performed feature-level evaluation where I calculated the ROC AUC score for each numerical feature to measure how well individual variables predicted conversion. The leading variable had an AUC score of 0.764. It means that this single feature alone can correctly distinguish between converted and non-converted leads about 76.4% of the time, which is better than random guessing (0.5) but not ideal.

2. I turned to ROC AUC score for the whole model. After training the logistic regression model, I computed validation accuracy and ROC AUC to assess overall predictive performance. I found the model score to be 0.82 while it had an accurace of 0.7 at 0.5 threshold.

3. I then did threshold analysis where I generated a precision–recall curve for 99 thresholds from 0.1 to 0.99. I plotted these to identify the optimal balance, that is the threshold where precision and recall intersected. At the threshold of 0.64, the model was equally good at identifying true positives and avoiding false positives. If I used this threshold instead of the default 0.5, I would slightly raise the bar for predicting converted leads.

4. I calculated F1 optimization as the next step. I computed the F1-score across thresholds and selected the one giving the highest F1 for best trade-off between precision and recall. The threshold was 0.57, which higher than the selected threshold of 0.5 but lower than 0.64 which was suggested by the precision-recall curve.

5. The final evaluation metric was cross-validation. I performed 5-fold cross-validation (with the `KFold` package from `scikit-learn` library) to evaluate model stability and compared AUC scores across different regularization strengths (C values). The standard deviation of the scores was 0.011 across the folds and different regularization strengths.
---

## Final Thoughts
The module gave me a lot to think about when it comes to model evaluation. I was familiar with the F1 scores from my bachelors studies but I realized that it is not the best metric to use. In fact, there was no single metric that is the industry standard. The most interesting lesson I came out with is that model development is iterative. The initial model is most likely not good enough. These metrics can help improve it.
