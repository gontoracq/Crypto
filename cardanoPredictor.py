import investpy
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, cross_val_predict

from tkinter import *
from tkinter import ttk

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

    #Performance
    scores = cross_val_score(lin_reg, X, y, cv=4)

    return (y_pred,scores.mean())

def __init__(self):

    datos = load_Data()
    datos_preparados = prepare_Data(datos)

    window = Tk()
    window.title("Cardano Prediction")
    window.geometry('500x400')
    window.configure(background = "#5353ec")
    a = Label(window ,text = "High").grid(row = 0,column = 0, padx=10, pady=10,sticky="")
    #a1 = Entry(window).grid(row = 0,column = 1)

    a1 = Entry(window, width=10)
    a1.grid(row=0, column=1, padx=10, pady=10, sticky = "")

    def submit():
        
        resultado = a1.get()
        
        resultado_numeric = float(resultado)
        
        reshaped_rs = [[resultado_numeric]]
        
        pred_submit = time_series_model_lr(datos_preparados, reshaped_rs)

        label_pred = Label(window ,text = 'Cardano might close -> ' + str(pred_submit[0]) +
        ' with a probability of ' + str(pred_submit[1]*100) + '%').place(relx = 0.5, rely = 0.5, anchor = CENTER)

        return label_pred  

    btn = ttk.Button(window ,text="Submit", command = submit).grid(row=0,column=2, sticky = "")
    window.mainloop()
