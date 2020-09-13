import streamlit as st
import pandas as pd
import xlrd

st.title("Enter Your SAT SCORE")

user_input = st.text_input("1350+ Scores are accepted by top US Universities")


DATA_URL = r'sat.xlsx'

##df = pd.read_excel(open('//X/str/Db/C/Source/selection/Date/Test/12.xlsx','rb'), sheetname='Sheet 1')


df = pd.read_excel(DATA_URL)



if user_input!="":
    val = int(user_input)
    st.dataframe(df[df['Scores']<val])

else :
    st.write("Results will show up here")