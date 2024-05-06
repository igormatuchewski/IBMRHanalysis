# Importing libs
import pandas as pd
import streamlit as st
import webbrowser as wb

# Configuring Streamlit page options
st.set_page_config(
    page_title='Home - IBM RH',
    page_icon='https://www.ibm.com/brand/experience-guides/developer/8f4e3cc2b5d52354a6d43c8edba1e3c9/02_8-bar-reverse.svg',
    layout='wide'
)

# Decreasing Streamlit padding size
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)



st.sidebar.markdown('Made by [Igor Matuchewski](https://www.linkedin.com/in/igor-matuchewski)')
st.sidebar.markdown('Click [here to see my Portfolio](https://sites.google.com/view/igormatuchewski/home)')
st.markdown('## IBM Dataset - Analysis of our Employees')
btn = st.button('Click here to acess the Dataset')
if btn:
    wb.open_new_tab('https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/data')

st.markdown("## __About project")
st.write('I simulated a demand in real life to practice my Python abilities, because that you will see I writing something like "I received a database from my boss", is just to train. I used some libraries like Pandas, Streamlit and Plotly Express!')
st.markdown('## __The problem')
st.write('My boss sending me a database with some RH informations about the company employees and asked me for a dashboard and some preview analysis.. the main objective is understand why we have so many unsatisfied employees with company.')
st.write('With this, I saw the oportunity to develop a dashboard that will answer my boss question and help the RH with rotines informations, and with this dashboard I can do all this things.')
st.write('This project was made 100% with Python, since the data processing using Pandas library until the graphics with Plotly Express library. I used too a VS Code extension that I can simulate a Jupyter Notebook, this helped me to made some adjusts in database along the project.')
st.write('If you have some question, suggestion or constructive critic, please contact me in my LinkedIn, the link is in sidebar in your left, just click in the link. Also, connect with me to generate more network, you will be welcome!')
st.write('Also, if you want, you can see all my Data Analitycs portfolio, the link is below my LinkedIn link, in the sidebar.')