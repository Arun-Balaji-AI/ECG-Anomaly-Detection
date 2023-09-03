from tensorflow.keras.models import load_model
from sklearn.utils import resample
import numpy as np 
import pandas as pd

def model_ecg(testing_data):
    model = load_model('ECG_Anomaly_Detection.h5')

    data = testing_data
    
    data = np.array(data)

    data = data.reshape(-1 , 187 , 1)

    pred = model.predict(data)

    classes = ['Normal Beats','Superventrical Ectopic Beats' , ' Ventricular Ectopic Beats' , 'Fusion Beats' , 'Unknown Beats']

    index = np.argmax(pred)


    return classes[index]


