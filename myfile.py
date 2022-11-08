import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv('data.csv')
rfc=RandomForestClassifier()
le=LabelEncoder()
data['le']=le.fit_transform(data['label'])
xtr,xtes,ytr,ytes=train_test_split(data.iloc[:,:7],data.iloc[:,-1])
fit=rfc.fit(xtr,ytr)
st.write(rfc.score(xtes,ytes))
def input_fun():
    N=st.number_input('Enter Nitrogen Value')
    P=st.number_input('Enter Phosphorus Value')
    K=st.number_input('Enter Potassium Value')
    tem=st.number_input('Enter Temperature Value')
    hum=st.number_input('Enter Humidity Value')
    ph=st.number_input('Enter PH Value')
    rainfall=st.number_input('Enter RainFall Value')
    values=np.array([[N,P,K,tem,hum,ph,rainfall]])
    le=LabelEncoder()
    l=le.fit_transform(data['label'])
    if st.button('Predict'):
        result=le.inverse_transform(rfc.predict(values))
        st.write(result)
input_fun()