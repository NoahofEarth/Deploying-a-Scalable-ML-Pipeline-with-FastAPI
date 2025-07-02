# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model uses a Random Forest Classifier trained to predict whether a person earns more than $50K/year using U.S. Census data. It utilizes demographic and work provided by the census data. The model is used in Python using scikit-learn

## Intended Use
This model is for educational purposes to show how to construct a ML pipeline through slice-based metrics. It is not intended for use in the real-world.

## Training Data
The model was trained on data from data/census.csv. This dataset contains records from the U.S. Census and includes categorical and numerical features.

## Evaluation Data
The evaluation was conducted on 20% test split from the default dataset. The test data was preprocessed using the same methods used the training data.

## Metrics
Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863

## Ethical Considerations
The model may reflect biases in the U.S. Census dataset (gender/racial income disparities). This model should not be used without fairness and mitigation steps.
## Caveats and Recommendations
 The dataset may be outdated. Future improvements could include feature engineering and bias mitigation steps