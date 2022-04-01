import streamlit as st
st.title('Hello 	:scream:')
st.button('Click aquí')
st.balloons()
st.markdown("$ \int_0^5 $")

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig
st.image('1tqn-min.png', caption='Sunrise by the mountains')

x = np.linspace(-10,10,100,dtype=float)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)
fig

import time

my_bar = st.progress(0)

#for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)#

#st.snow()     
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
