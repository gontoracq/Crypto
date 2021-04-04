from tkinter import *
from tkinter import ttk
from model import load_Data, prepare_Data, time_series_model_lr

datos = load_Data()
datos_preparados = prepare_Data(datos)

window = Tk()
window.title("Cardano Prediction")
window.geometry('325x250')
window.configure(background = "#5353ec")
a = Label(window ,text = "High").grid(row = 0,column = 0, padx=10, pady=10)
#a1 = Entry(window).grid(row = 0,column = 1)

a1 = Entry(window, width=10)
a1.grid(row=0, column=1, sticky=W, padx=10, pady=10)

def submit():
     
    resultado = a1.get()
    
    resultado_numeric = float(resultado)
    
    reshaped_rs = [[resultado_numeric]]
    
    pred_submit = time_series_model_lr(datos_preparados, reshaped_rs)

    label_pred = Label(window ,text = 'Cardano might close -> ' + str(pred_submit)).place(relx = 0.5, rely = 0.5, anchor = CENTER)

    return label_pred  

btn = ttk.Button(window ,text="Submit", command = submit).grid(row=0,column=2)
window.mainloop()

