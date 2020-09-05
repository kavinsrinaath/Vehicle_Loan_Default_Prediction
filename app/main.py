#to handle data
import pickle
from pydantic import BaseModel
import numpy as np

#import joblib

#from sklearn.ensemble import GradientBoostingClassifier

#Server
import uvicorn
from fastapi import FastAPI


app = FastAPI()

#loading files

model = pickle.load(open('app/vc_loan_modelv1.pickle','rb'))
#clf = joblib.load
features = pickle.load(open('app/features.pickle','rb'))

class Data(BaseModel):
    disbursed_amount : int
    asset_cost : int
    ltv : float
    branch_id : int
    supplier_id : int
    manufacturer_id : int
    Current_pincode_ID : int
    Employment_Type : int
    State_ID : int
    Employee_code_ID : int
    PERFORM_CNS_SCORE : int
    PERFORM_CNS_SCORE_DESCRIPTION : int
    NEW_ACCTS_IN_LAST_SIX_MONTHS : int
    DELINQUENT_ACCTS_IN_LAST_SIX_MONTHS : int
    AVERAGE_ACCT_AGE : float
    CREDIT_HISTORY_LENGTH : float
    NO_OF_INQUIRIES : int
    Age : float
    Age_of_Loan : float
    No_of_Proofs : int
    Total_ACCTS : int
    Total_Active_ACCTS : int
    Total_Overdue_ACCTS : int
    Total_CurrentBalance : int
    Total_SanctionedAmount : int
    Total_DisbursedAmount : int
    Total_InstalAmount : int
    class Config:
        schema_extra = {
            "example": {
                "disbursed_amount" : 56032,
                "asset_cost" : 15000,
                "ltv" : 66.3,
                "branch_id" : 68,
                "supplier_id" : 21054,
                "manufacturer_id" : 45,
                "Current_pincode_ID" : 6673,
                "Employment_Type" : 2,
                "State_ID" : 6,
                "Employee_code_ID" : 849,
                "PERFORM_CNS_SCORE" : 660.35,
                "PERFORM_CNS_SCORE_DESCRIPTION" : 1.00,
                "NEW_ACCTS_IN_LAST_SIX_MONTHS" : 1.00,
                "DELINQUENT_ACCTS_IN_LAST_SIX_MONTHS" : 1.00,
                "AVERAGE_ACCT_AGE" : 0.85,
                "CREDIT_HISTORY_LENGTH" : 1.20,
                "NO_OF_INQUIRIES" : 2.00,
                "Age" : 28.4,
                "Age_of_Loan" : 2.6,
                "No_of_Proofs" : 2,
                "Total_ACCTS" : 4,
                "Total_Active_ACCTS" : 2,
                "Total_Overdue_ACCTS" : 0,
                "Total_CurrentBalance" : 185642,
                "Total_SanctionedAmount" : 45000,
                "Total_DisbursedAmount" : 12000,
                "Total_InstalAmount" : 1300
            }
        }



@app.post("/predict",
responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {"prediction": "The loan applicant will pay the 1st EMI"}
                }
            },
        },
    },
)
async def predict(data:Data):
    
    #to extract data in correct order
    data_dict = data.dict()
    to_predict = [data_dict[feature] for feature in features]
    to_predict = np.array(to_predict)
    
    #predecting the output using the model
    prediction = model.predict(to_predict.reshape(1,-1))
    if prediction[0] == 1:
        return {"prediction":"The loan applicant will pay the 1st EMI"}
    else:
        return {"prediction":"The loan applicant will default on 1st EMI payment"}
    #return {"prediction":int(prediction[0])}