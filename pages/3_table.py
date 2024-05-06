# Importing libs
import pandas as pd
import plotly_express as px
import streamlit as st

#  Configuring Streamlit page options
st.set_page_config(
    page_title='Dashboard - IBM RH',
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

# Reading dataset
# Checking if 'dtset' is not in session_state or if it is not a Dataframe
if 'dtset' not in st.session_state or not isinstance(st.session_state['dtset'], pd.DataFrame):
    # Carrega o DataFrame a partir do arquivo CSV
    df_ibm = pd.read_csv('dataset/df_ibm.csv')
    # Storing the Dataframe in session_state for later use
    st.session_state['dtset'] = df_ibm
else:
    # If 'dtset' already is in session_state and is a valid Dataframe, just retrieve it
    df_ibm = st.session_state['dtset']

## Sidebar content
# Status filter
status = sorted(df_ibm['Unsatisfied'].unique())
status.insert(0, "All") 
selected_status = st.sidebar.selectbox('Select a status', status)
# Gender filter
genders = sorted(df_ibm['Gender'].unique())
genders.insert(0, "Both")
selected_gender = st.sidebar.selectbox('Select an Gender', genders)
# Marital Status Filter
maritals = sorted(df_ibm['MaritalStatus'].unique())
maritals.insert(0, "All")
selected_marital = st.sidebar.multiselect('Select an Marital Status', maritals, default='All')
# YearsSinceLastPromotion Range Filter
promotions = sorted(df_ibm['YearsSinceLastPromotionRange'].unique())
promotions.insert(0, "All")
selected_promotion = st.sidebar.multiselect('Years Since Last Promotion Range', promotions, default='All')
# Age Filter
min_age = int(df_ibm['Age'].min())
max_age = int(df_ibm['Age'].max())
age = st.sidebar.slider('Age', min_age, max_age, (min_age, max_age))
# Income Filter
min_income = int(df_ibm['MonthlyIncome'].min())
max_income = int(df_ibm['MonthlyIncome'].max())
income = st.sidebar.slider('Monthly Income', min_income, max_income, (min_income, max_income))


df_filtered = df_ibm.copy()

### Variables
## Setting a filtered df based on selected status and gender
if 'All' not in selected_status:
    df_filtered = df_filtered[df_filtered['Unsatisfied'] == selected_status]

if selected_gender != 'Both':
    df_filtered = df_filtered[df_filtered['Gender'] == selected_gender]

if 'All' not in selected_marital:
    if selected_marital:
        df_filtered = df_filtered[df_filtered['MaritalStatus'].isin(selected_marital)]
    else:
        df_filtered = df_filtered.copy()
else:
    df_filtered = df_filtered.copy()

if 'All' not in selected_promotion:
    if selected_promotion:
        df_filtered = df_filtered[df_filtered['YearsSinceLastPromotionRange'].isin(selected_promotion)]
    else:
        df_filtered = df_filtered.copy()
else:
    df_filtered = df_filtered.copy()

df_filtered = df_filtered[(df_filtered['MonthlyIncome'] >= income[0]) & (df_filtered['MonthlyIncome'] <= income[1])]
df_filtered = df_filtered[(df_filtered['Age'] >= age[0]) & (df_filtered['Age'] <= age[1])]

st.markdown('## __Table')
st.markdown('##')

df_filtered