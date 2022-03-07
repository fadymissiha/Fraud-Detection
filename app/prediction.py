# For sample predict functions for popular libraries visit https://github.com/opendatahub-io/odh-prediction-samples

# Import libraries
import pandas as pd
import cloudpickle as cp


# Load your model.
pipeline = cp.load(open('DecisionTree.pkl', 'rb'))


def predict(args_dict):
    tran = { 'CASH_OUT': args_dict.get('CASH_OUT'), 'amount': args_dict.get('amount'), 'oldbalanceOrg': args_dict.get('oldbalanceOrg'), 'newbalanceOrig': args_dict.get('newbalanceOrig'), 'oldbalanceDest': args_dict.get('oldbalanceDest'), 'newbalanceDest': args_dict.get('newbalanceDest') }
    
    df = pd.DataFrame(tran, index=[0])
    prediction = pipeline.predict(df)[0]

    return str({'isFraud': prediction})



