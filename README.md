# Project of python data analysis using drug consumption data set

## Task

* Data visualization
* Data cleaning
* Modeling
* Flask API

## Problem 
Use given attributes to predict the drug consumption situation. Use binary classification by union of part of classes into one new class. "Never Used" and "Used over a Decade Ago" form class "Non-user" and all other classes form class "User".

### Data visualization
Using matplotlib and seaborn libraries to show relations between different variables and the targets. 

For example : count of different classes for each drug, heat map showing correlation between the features, gender/age/education/ethnicity/country percentage comparaison, cross table using country and gender and ethnicity, relations between education/ethnicity and alcohol target, gender/age and cannabis/legal highs target, age and ecstasy target, pie chart of the frequency of using nicotine, number of observation and frequency for every consumption level of every drug, etc.

### Data cleaning 
Changing drug classes into integer, rename columns, drop columns with low depedencies : nscore,escore,oscore,ascore,cscore and impulsive, convert some columns to string type and update data, modifying target into 0/1, etc.

### Modeling
Use the scikit-learn library, use different algorithms, different
hyper parameters, do grid search.

Make train set and test set, scale the data, plot confusion matrix of the prediction, compare accurancy.

Models used : Logistic regression, ridge classifier, support vector machines, random forest classifier.

### Flask API
Transformation of the model into flask API. 

Save the model as pickle file, so that later to use it and call the predict function to get a prediction for the new input data. When running the logistic_api.py it first loads the created logistic pickle file. Predictions are made by passing a post JSON request to the created Flask web server which is on port 5000 by default. In logistic_api.py this request is received and a prediction is based on the already loaded prediction function of the model. It returns the prediction in JSON format.

Test example : 

Send Post [[0.96082,-0.31685,-0.46725,0.80523,-0.84732,-1.01450,-1.37983,0.40148,0,0,0,3,4,0,0,0,0,0,0,0,1,0,0,0]] we got a prediction of class 1 as output of the model. 

Send Post [[0.24923,-0.31685,-0.67825,-0.30033,-1.55521,1.63088,-1.37983,-1.54858,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]] we got a prediction of class 0 as output of the model. 

This API can be easily used by other people to use the machine learning model to get the results.
