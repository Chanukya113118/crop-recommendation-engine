import pickle
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder
model=pickle.load(open('model.pkl','rb'))
data=pd.read_excel('data.xlsx')
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
        result=le.inverse_transform(model.predict(values))
        st.header('Dear Farmer you are recommended to cultivate')
        st.success(result[0])
        st.balloons()
if __name__=='__main__':
    st.title('Crop Recommendation Engine')
    st.warning('Recommended crop is just based on Soil Fertility')
    input_fun()