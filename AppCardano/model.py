import investpy
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def load_Data():
    input_var_todayDate = datetime.today().strftime('%d/%m/%Y')

    data = investpy.get_crypto_historical_data(crypto='cardano', from_date='31/12/2017', to_date=input_var_todayDate)

    data = data.drop(columns=['Currency'])

    return data

def prepare_Data(cardano_hst):

    #Separate the Date attribute into 3 new attributes Year, Month and Day
    cardano_hst['Year'] = cardano_hst.index.year
    cardano_hst['Month'] = cardano_hst.index.month
    cardano_hst['Day'] = cardano_hst.index.day

    return cardano_hst

def time_series_model_lr(train, input_data):
    y = train.Close
    predictor_col = ['High']

    # Create training predictors data
    X = train[predictor_col]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = .25, random_state =33)

    # LinearRegression
    lin_reg = LinearRegression(normalize=True, n_jobs=-1)
    lin_reg.fit(X_train, y_train)
    #Prediction
    y_pred = lin_reg.predict(input_data)

    return y_pred