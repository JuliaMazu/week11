import streamlit as st

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name:")
name_length = len(name)
st.write("Your name has ",name_length, "characters")




#viz_correlation = sns.heatmap(df_weather.corr(), 
								#center=0,
								#cmap = sns.color_palette("vlag", as_cmap=True)
								#)

#st.pyplot(viz_correlation.figure)