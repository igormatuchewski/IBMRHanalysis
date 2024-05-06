# Importing libs
import pandas as pd
import streamlit as st
import plotly_express as px

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

## _____Personal
# Unsatisfied Employees x Gender
unsEmpXgend = df_filtered.groupby('Gender')['Unsatisfied'].count().sort_values(ascending=False)
# Unsatisfied Employees x MaritalStatus
unsEmpxmart = df_filtered.groupby('MaritalStatus')['Unsatisfied'].count().sort_values(ascending=False)
# Unsatisfied Employees x IncomeRange
unsEmpxmInc = df_filtered.groupby('IncomeRange')['Unsatisfied'].count().sort_values(ascending=False)
# Unsatisfied Employees x DistanceRange
unsEmpxdist = df_filtered.groupby('DistanceRange')['Unsatisfied'].count().sort_values(ascending=True)
# Unsatisfied Employees x AgeRange
unsEmpxAge = df_filtered.groupby('AgeRange')['Unsatisfied'].count().sort_values(ascending=False)

## _____Job
# Employees Unsatisfied or not Count
emp_count = df_ibm['Unsatisfied'].value_counts().reset_index().sort_values(by='Unsatisfied', ascending=False)
emp_count.columns = ['Unsatisfied', 'Count']
# Unsatisfied Employees x Department
unsEmpXdept = df_filtered.groupby('Department')['Unsatisfied'].count().sort_values(ascending=True)
# Unsatisfied Employees x EducationField
unsEmpXeduc = df_filtered.groupby('EducationField')['Unsatisfied'].count().sort_values(ascending=False)
# Unsatisfied Employees x JobSatisfaction
unsEmpXjobS = df_filtered.groupby('JobSatisfaction')['Unsatisfied'].count().sort_values(ascending=False)
# Unsatisfied Employees x Performance Rating
unsEmpXperf = df_filtered.groupby('PerformanceRating')['Unsatisfied'].count().sort_values(ascending=False)
# Unsatisfied Employees x YearsAtCompany
unsEmpxyAc = df_filtered.groupby('YearsAtCompanyRange')['Unsatisfied'].count().sort_values(ascending=True)
# Unsatisfied Employees x YearsInCurrRoleRange
unsEmpxyIcR = df_filtered.groupby('YearsInCurrRoleRange')['Unsatisfied'].count().sort_values(ascending=False)
# Unsatisfied Employees x YearsWithCurrManagerRange
unsEmpxyIcM = df_filtered.groupby('YearsWithCurrManagerRange')['Unsatisfied'].count().sort_values(ascending=False)
# Unsatisfied Employees x YearsSinceLastPromotionRange
unsEmpxySlP = df_filtered.groupby('YearsSinceLastPromotionRange')['Unsatisfied'].count().sort_values(ascending=True)
# Unsatisfied Employees x RelationshipSatisfaction
unsEmpxReSf = df_filtered.groupby('RelationshipSatisfaction')['Unsatisfied'].count().sort_values(ascending=False)
# Unsatisfied Employees x BusinessTravel
unsEmpxBuss = df_filtered.groupby('BusinessTravel')['Unsatisfied'].count().sort_values(ascending=False)


#### Graphics
### _____Personal
# Employees x Unsatisfied
# colors = ['#ed2ad6' if gender == 'Female' else '#4287f5' for gender in unsEmpXgend.index]
# empXuns_graph = px.bar(emp_count, x='Unsatisfied', y='Count', title='Count of Employees | Status', text_auto=True, color_discrete_sequence=['#FE596A'], labels={
#     'Unsatisfied' : 'Status'
# })
# empXuns_graph.update_traces(textfont=dict(size=12, color='white'))
# Unsatisfied Employees x Gender
total = unsEmpXgend.sum()
percentages = (unsEmpXgend / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpXgend.values, percentages)]
colors = ['#ed2ad6' if gender == 'Female' else '#4287f5' for gender in unsEmpXgend.index]
unsEmpXgend_graph = px.bar(unsEmpXgend, x=unsEmpXgend.index, y=unsEmpXgend.values, title='Unsatisfied Employees | Gender', text=text_values, text_auto=True, color_discrete_sequence=colors, labels={
    'y' : 'Count of Unsatisfied Employees',
    'x' : 'Gender'
})
unsEmpXgend_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textposition='outside', marker_color=colors)
unsEmpXgend_graph.update_yaxes(range=[0, unsEmpXgend.values.max() * 1.1]) # here I defined a y to be 10% higher then the max value present in the context
# Unsatisfied Employees x MartialStatus
perf_colors = ['#FE596A', '#B3B04F', '#034579']
unsEmpxmart_graph = px.pie(unsEmpxmart, values=unsEmpxmart.values, names=unsEmpxmart.index, title='"%" and Count of Unsatisfied Employees | Job Satisfaction' ,color_discrete_sequence=perf_colors)
unsEmpxmart_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textinfo='percent+label+value', pull=[0.03, 0.03, 0.03, 0.03])
unsEmpxmart_graph.update_layout(legend=dict(orientation='h', yanchor='bottom', xanchor='center', y=1.02, x=0.5))
# Unsatisfied Employees x IncomeRange
total = unsEmpxmInc.sum()
percentages = (unsEmpxmInc / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpxmInc.values, percentages)]
max_index = unsEmpxmInc.values.argmax()
colors = ['#FE596A' if i == max_index else '#f78f99' for i in range(len(unsEmpxmInc.index))]
unsEmpxmInc_graph = px.bar(x=unsEmpxmInc.index, y=unsEmpxmInc.values, title='Unsatisfied Employees | Monthly Income', text=text_values, text_auto=True, color_discrete_sequence=colors, labels={
    'y' : 'Count of Unsatisfied Employees',
    'x' : 'Monthly Income'
})
unsEmpxmInc_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textposition='outside',  marker_color=colors)
unsEmpxmInc_graph.update_yaxes(range=[0, unsEmpxmInc.values.max() * 1.1])
# Unsatisfied Employees x DistanceRange 
perf_colors = ['#FE596A', '#B3B04F', '#034579', '#569BA0']
unsEmpxdist_graph = px.pie(unsEmpxdist, values=unsEmpxdist.values, names=unsEmpxdist.index, title='"%" and Count of Unsatisfied Employees | Distance from Home' ,color_discrete_sequence=perf_colors)
unsEmpxdist_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textinfo='percent+label+value', pull=[0.03, 0.03, 0.03, 0.03])
unsEmpxdist_graph.update_layout(legend=dict(orientation='h', yanchor='bottom', xanchor='center', y=1.02, x=0.5))
# Unsatisfied Employees x AgeRange
total = unsEmpxAge.sum()
percentages = (unsEmpxAge / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpxAge.values, percentages)]
max_index = unsEmpxmInc.values.argmax()
colors = ['#FE596A' if i == max_index else '#f78f99' for i in range(len(unsEmpxmInc.index))]
unsEmpxAge_graph = px.bar(x=unsEmpxAge.index, y=unsEmpxAge.values, title='Unsatisfied Employees | Age', text=text_values, text_auto=True, color_discrete_sequence=colors, labels={
    'y' : 'Count of Unsatisfied Employees',
    'x' : 'Age'
})
unsEmpxAge_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textposition='outside', marker_color=colors)
unsEmpxAge_graph.update_yaxes(range=[0, unsEmpxAge.values.max() * 1.1])

### _____Job
# Unsatisfied Employees x Department 
total = unsEmpXdept.sum()
percentages = (unsEmpXdept / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpXdept.values, percentages)]
max_index = unsEmpXdept.idxmax()
colors = ['#FE596A' if idx == max_index else '#f78f99' for idx in unsEmpXdept.index]
unsEmpXdept_graph = px.bar(x=unsEmpXdept.values, y=unsEmpXdept.index, title='Unsatisfied Employees | Department', text=text_values, text_auto=True, color_discrete_sequence=colors, labels={
    'x' : 'Count of Unsatisfied Employees',
    'y' : 'Department'
}, orientation='h')
unsEmpXdept_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), marker_color=colors)
# Unsatisfied Employees x YearsAtCompany 
total = unsEmpxyAc.sum()
percentages = (unsEmpxyAc / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpxyAc.values, percentages)]
max_index = unsEmpxyAc.idxmax()
colors = ['#FE596A' if idx == max_index else '#f78f99' for idx in unsEmpxyAc.index]
unsEmpxyAc_graph = px.bar(x=unsEmpxyAc.values, y=unsEmpxyAc.index, title='Unsatisfied Employees | Years At Company', text=text_values, text_auto=True, color_discrete_sequence=colors, labels={
    'x' : 'Count of Unsatisfied Employees',
    'y' : 'Years At Company'
}, orientation='h')
unsEmpxyAc_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textposition='outside', marker_color=colors)
# Unsatisfied Employees x YearsSinceLastPromotion 
total = unsEmpxySlP.sum()
percentages = (unsEmpxySlP / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpxySlP.values, percentages)]
max_index = unsEmpxySlP.idxmax()
colors = ['#FE596A' if idx == max_index else '#f78f99' for idx in unsEmpxySlP.index]
unsEmpxySlP_graph = px.bar(x=unsEmpxySlP.values, y=unsEmpxySlP.index, title='Unsatisfied Employees | Years Without Promotion ', text=text_values, text_auto=True, color_discrete_sequence=colors, labels={
    'x' : 'Count of Unsatisfied Employees',
    'y' : 'Years Without Promotion'
}, orientation='h')
unsEmpxySlP_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textposition='outside', marker_color=colors)
# Unsatisfied Employees x PerformanceRating
total = unsEmpXperf.sum()
percentages = (unsEmpXperf / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpXperf.values, percentages)]
max_index = unsEmpXperf.values.argmax()
colors = ['#FE596A' if i == max_index else '#f78f99' for i in range(len(unsEmpXperf.index))]
unsEmpXperf_graph = px.bar(x=unsEmpXperf.index, y=unsEmpXperf.values, title='Unsatisfied Employees | Performance', text=text_values, text_auto=True, color_discrete_sequence=['#FE596A'], labels={
    'y' : 'Count of Unsatisfied Employees',
    'x' : 'Performance Rating'
})
unsEmpXperf_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textposition='outside', marker_color=colors)
unsEmpXperf_graph.update_yaxes(range=[0, unsEmpXperf.values.max() * 1.1])
# Unsatisfied Employees x JobSatisfaction 
                #red       #green     #blue      #lightblue
perf_colors = ['#FE596A', '#B3B04F', '#034579', '#569BA0']
unsEmpXjobS_graph = px.pie(unsEmpXjobS, values=unsEmpXjobS.values, names=unsEmpXjobS.index, title='"%" and Count of Unsatisfied Employees | Job Satisfaction' ,color_discrete_sequence=perf_colors)
unsEmpXjobS_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textinfo='percent+label+value', pull=[0.03, 0.03, 0.03, 0.03])
unsEmpXjobS_graph.update_layout(legend=dict(orientation='h', yanchor='bottom', xanchor='center', y=1.02, x=0.5))
# Unsatisfied Employees x RelationshipSatisfaction 
                #red       #green     #blue      #lightblue
perf_colors = ['#FE596A', '#B3B04F', '#034579', '#569BA0']
unsEmpxReSf_graph = px.pie(unsEmpxReSf, values=unsEmpxReSf.values, names=unsEmpxReSf.index, title='"%" and Count of Unsatisfied Employees | Relationship Satisfaction' ,color_discrete_sequence=perf_colors)
unsEmpxReSf_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textinfo='percent+label+value', pull=[0.03, 0.03, 0.03, 0.03])
unsEmpxReSf_graph.update_layout(legend=dict(orientation='h', yanchor='bottom', xanchor='center', y=1.02, x=0.5))
# Unsatisfied Employees x EducationField
total = unsEmpXeduc.sum()
percentages = (unsEmpXeduc / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpXeduc.values, percentages)]
unsEmpXeduc_graph = px.funnel(x=unsEmpXeduc.values, y=unsEmpXeduc.index, title='Unsatisfied Employees | Education Field', text=text_values, labels={
    'y' : 'Education Field'
}, color_discrete_sequence=['#FE596A'])
unsEmpXeduc_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'))
# Unsatisfied Employees x YearsAtCurrRole
total = unsEmpxyIcR.sum()
percentages = (unsEmpxyIcR / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpxyIcR.values, percentages)]
max_index = unsEmpxyIcR.values.argmax()
colors = ['#FE596A' if i == max_index else '#f78f99' for i in range(len(unsEmpxyIcR.index))]
unsEmpxyIcR_graph = px.bar(x=unsEmpxyIcR.index, y=unsEmpxyIcR.values, title='Unsatisfied Employees | Years In Same Role', text=text_values, text_auto=True, color_discrete_sequence=['#FE596A'], labels={
    'y' : 'Count of Unsatisfied Employees',
    'x' : 'Years In Current Role'
})
unsEmpxyIcR_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textposition='outside', marker_color=colors)
unsEmpxyIcR_graph.update_yaxes(range=[0, unsEmpxyIcR.values.max() * 1.1])
# Unsatisfied Employees x YearsWithCurrManager
total = unsEmpxyIcM.sum()
percentages = (unsEmpxyIcM / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpxyIcM.values, percentages)]
max_index = unsEmpxyIcM.values.argmax()
colors = ['#FE596A' if i == max_index else '#f78f99' for i in range(len(unsEmpxyIcM.index))]
unsEmpxyIcM_graph = px.bar(x=unsEmpxyIcM.index, y=unsEmpxyIcM.values, title='Unsatisfied Employees | Years With Current Manager', text=text_values, text_auto=True, color_discrete_sequence=['#FE596A'], labels={
    'y' : 'Count of Unsatisfied Employees',
    'x' : 'Years With Current Manager'
})
unsEmpxyIcM_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textposition='outside', marker_color=colors)
unsEmpxyIcM_graph.update_yaxes(range=[0, unsEmpxyIcM.values.max() * 1.1])
# Unsatisfied Employees x BusinessTravel
total = unsEmpxBuss.sum()
percentages = (unsEmpxBuss / total) * 100
text_values = [f'{count} ({percentage:.2f}%)' for count, percentage in zip(unsEmpxBuss.values, percentages)]
max_index = unsEmpxBuss.values.argmax()
colors = ['#FE596A' if i == max_index else '#f78f99' for i in range(len(unsEmpxBuss.index))]
unsEmpxBuss_graph = px.bar(x=unsEmpxBuss.index, y=unsEmpxBuss.values, title='Unsatisfied Employees | Business Travel', text=text_values, text_auto=True, color_discrete_sequence=['#FE596A'], labels={
    'y' : 'Count of Unsatisfied Employees',
    'x' : 'Frequency'
})
unsEmpxBuss_graph.update_traces(textfont=dict(size=12, color='white', family='Arial'), textposition='outside', marker_color=colors)
unsEmpxBuss_graph.update_yaxes(range=[0, unsEmpxBuss.values.max() * 1.1])

## Plotting Graphs
# Defining columns
st.markdown('# __General')
# st.plotly_chart(empXuns_graph, use_container_width=True)
st.markdown('## __Personal Informations')
col1, col2, col3 = st.columns(3)
col1.plotly_chart(unsEmpXgend_graph, use_container_width=True)
col2.plotly_chart(unsEmpxAge_graph, use_container_width=True)
col3.plotly_chart(unsEmpxmInc_graph, use_container_width=True)

col4, col5 = st.columns(2)
col4.plotly_chart(unsEmpxmart_graph, use_container_width=True)
col5.plotly_chart(unsEmpxdist_graph, use_container_width=True)

st.markdown('## __Job Informations')

col4, col5, col6 = st.columns(3)
col4.plotly_chart(unsEmpXperf_graph, use_container_width=True)
col5.plotly_chart(unsEmpxBuss_graph, use_container_width=True)
col6.plotly_chart(unsEmpxyIcR_graph, use_container_width=True)

col7, col8 = st.columns(2)
col7.plotly_chart(unsEmpXeduc_graph, use_container_width=True)
col8.plotly_chart(unsEmpXjobS_graph, use_container_width=True)

col9, col10 = st.columns(2)
col9.plotly_chart(unsEmpXdept_graph, use_container_width=True)
col10.plotly_chart(unsEmpxReSf_graph, use_container_width=True)

col11, col12, col13 = st.columns(3)
col11.plotly_chart(unsEmpxyIcM_graph, use_container_width=True)
col12.plotly_chart(unsEmpxyAc_graph, use_container_width=True)
col13.plotly_chart(unsEmpxySlP_graph, use_container_width=True)

st.sidebar.markdown('Made by [Igor Matuchewski](https://www.linkedin.com/in/igor-matuchewski)')
