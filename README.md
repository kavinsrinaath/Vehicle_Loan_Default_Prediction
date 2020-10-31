**Vehicle Loan Default Prediction**

**Objective:**

To build a model that is capable of predicting whether a person will default on his/her first EMI payment of vehicle loan.

**Client/End User:**

The end user Larsen &amp; Toubro Financial Services (LTFS) will have a deeper insight on decision making on sanctioning loan for a particular applicant. Such as the result given by the model will give more confidence when deciding.

**Data:**

We use LTFS&#39;s own data which they used to conduct a competition in 2019.The dataset contains about 53000 entries with features such as loan amount, asset cost, customer employment status etc. The dataset contains 40 independent columns with 1 dependent column which 0 or 1 as value. (0-Paid, 1-Default).

**Workflow outline:**

- **Data Wrangling**:
  -  Transformed data type for columns like DOB, DisbursalDate into proper date strings.
  -  Handled missing values in Employment Type column. NaN were replaced with &#39;unknown&#39; string.
  -  Employment type, PERFORM\_CNS.SCORE.DESCRIPTION columns had string values which were mapped to integers.
  -  ACCT.AGE,CREDIT.HISTORY.LENGTH columns had values like &#39;2 yrs 4months&#39;,replaced them with float values like 2.4 with a custom function yrscalc.
  -  lables column was created out of loan\_default column for easy human interpretation.

- **Feature Engineering/Selection:**
  -  Proofs columns were combined (summed up) to create a new feature called No.of.Proofs.
  -  The dataset faced imbalance class issue  with about 78%- Paid and 22% Default class. To handle it SMOTE from imblearn was used to overcome it.
  -  Using ExtraTressClassifer to obtain feature importance scores it was found that secondary account related features did not have much significance and hence primary and secondary account features were clubbed.


- **Model building**
  -  Using GridSearchCV, the models – RandomForestClassifier, GradientBoostingClassifier were tuned and the best scores were obtained.
  - ****Tuned parameters for Gradient Boosting are**** :
    - loss
    - learning\_rate
    - n\_estimators

    max\_depth here was dropped due to computational limits.

-
  - ****Tuned parameters for Random Forest are**** :
    - n\_estimators
    - max\_depth
    - criterion
  -  precision and recall are the metrics upon which the model is evaluated.
  -   A custom function was created that had the code for GridSearch which returns best params as well best best score.
  -  Obtained best params for Gradient Boosting:
    - loss : deviance
    - learning\_rate : 0.5
    - n\_estimators : 150
    - best score : 0.902
  -  Obtained best params for Random Forest:
    - n\_estimators : 650
    - max\_depth : 15
    - criterion : gini
    - best score : 0.823
  -  With the above result Gradient boosting was chosen for its significantly better performance over Random forest and tuned accordingly.
  -  Below is the classification report generated after prediction:

        |   | precision | recall | f1-score | support |
        | --- | --- | --- | --- | --- |
        | Paid | 0.77 | 0.96 | 0.86 | 45745 |
        | Default | 0.95 | 0.72 | 0.82 | 45745 |
        | accuracy |   |   | 0.84 | 91490 |
        | macro avg | 0.86 | 0.84 | 0.84 | 91490 |
        | weighted avg | 0.86 | 0.84 | 0.84 | 91490 |

-
  -  As we can see the model obtained is fairly good in predicting the loan defaults. Further tuning and exploration will definitely lead to better model.

- **Model Interpretation:**
  -  While we work towards achieving a high performing model, its equally important to understand why/how the model achieved the desired output/performance.
  -  We use SHAP library to do a basic analysis of how each feature contributed towards the model performance.
  -  Summary plot from SHAP is used to get an overall feature impact towards the model.


  - ****We will look at 5 features here****:

            Age.of.Loan - This one has 2 extremes where certain high and low  values either decrease or increase prediction. A manual investiga-tion is needed to find the cause.

            manufacturer\_id - Here mainly high values decrease prediction while low and mid-ranged values increase prediction.

            branch\_id -Lower values either tend to decrease prediction or have a small positive effect while high and mid-ranged values increase prediction.

            Total.ACCTS - Lower values highly tend to increase the    prediction of the model.

            PERFORM\_CNS\_SCORE - Certain low values and most high values decrease prediction while most lower values tend to increase  prediction.


- **API details:**
  - The API has been containerized using Docker. Using that it has been deployed on RedHat's PaaS product OpenShift and also on Heroku.
  - REST resource path : http://vcloanapp-modelone.apps.us-west-1.starter.openshift-online.com/predict or https://vc-loan-v1-beta.herokuapp.com
  - API swagger document: http://vcloanapp-modelone.apps.us-west-1.starter.openshift-online.com/docs or https://vc-loan-v1-beta.herokuapp.com/docs
  - The sample json request body from the swagger can be used for tryout or alternatively tools such as SOAP UI or Postman can also be used to consume the API.