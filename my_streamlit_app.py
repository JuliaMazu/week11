import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


st.title('Hello Wilders, welcome to my application!')

st.write("I want to show you some car statistique")

df = pd.read_csv('C:\\Users\\wilder\\Downloads\\cars.csv')

#Button and limit by year

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.header("Correlation between car characteristics")
st.button('Limit by the year', on_click=click_button)
if st.session_state.clicked:
    st.write('Between following values')
    year = st.slider('Select a value', min_value=1971, max_value=1983) 
    
if st.session_state.clicked == False:
    viz_pair = sns.pairplot(df[['mpg', 'hp', 'cylinders', 'weightlbs']])
else:
	viz_pair = sns.pairplot(df[df['year']==year][['mpg', 'hp', 'cylinders', 'weightlbs']])
st.pyplot(viz_pair.figure)


st.header("Correlation between weight of car and mpg")
viz1 = sns.jointplot(df, x = 'weightlbs', y = 'mpg', hue = 'continent', palette='PiYG')
st.pyplot(viz1.figure)

continent = st.selectbox(
    'Which continent would you like to verify?',
    ('US', 'Europe', 'Japan'))

diction = {'US' : ' US.',
           'Europe' : ' Europe.', 
        	'Japan' : ' Japan.'}

viz_heat = sns.heatmap(df[df['continent']==diction[continent]][['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60']].corr(),
            annot=True,
            annot_kws={'fontsize':8},
            cmap = 'PiYG',
            center=0, label = False
            )
st.pyplot(viz_heat.figure)


#image = Image.open(r"C:\Users\wilder\Documents\iCDpNj.jpg")
st.image('https://wallpapercave.com/wp/4OTQErU.jpg', caption='Nice ride')

