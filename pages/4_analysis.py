# Importing libs
import pandas as pd
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

st.sidebar.markdown('Made by [Igor Matuchewski](https://www.linkedin.com/in/igor-matuchewski)')
st.sidebar.markdown('Click [here to see my Portfolio](https://sites.google.com/view/igormatuchewski/home)')


st.markdown('# ___ Analysis')

st.write('## __Some relavant points for my analysis:')
st.write('### Total count of unsatisfied employees: 237')

st.write('* 63% of all unsatisfied employees are men;')
st.write('* 49% are between 26 and 35 years old;')
st.write('* 69% earn between 1k and 5k;')
st.write('* 51% are single;')
st.write('* 64% live near the company;')
st.write('* 100% of the unsatisfied employees have a nice performance, and 15% are outstanding;')
st.write('* 65% travek rarely;')
st.write('* 77% have been in the same role for 0 to 5 years;')
st.write('* there is not a great correlation, but 37% are from the life sciences field;')
st.write('* in job satisfaction, there is a great equilibrium; we have the same number satisfied and unsatisfied;')
st.write('* 56% are from Research & Development;')
st.write('* 76% have had the same manager for 0 to 5 years;')
st.write('* 91% of our employees have been with the company for 0 to 10 years.')

st.write('### __After that, I try to explore more of the main points:')
st.write('We have 237 unsatisfied employees, with 116 between 26 and 35 years old, and more than half of the unsatisfied employees who receive between 1k and 5k fall into this age range.')
st.write('We can verify that there is an important correlation here; probably people want to earn more, so why do not they have a promotion or something like that? As seen above, salary is an important factor in why our employees are dissatisfied with our company. Another view is that 114 employees earn between 1k and 3k. Is this really fair?')
st.write('I also checked that the majority of unsatisfied employees live near the company, so this can not be the main reason for all the dissatisfaction. However, 73 people live far away, and this is good to verify. How much time do they spend coming here? Maybe we can offer a hybrid work model for them.')
st.write('Another point is that 70% rarely or do not travel. Do they want to travel more? What is the criterion for defining who will travel? Who chooses? Also, for the employees who travel frequently, maybe they are tired from too many trips. We need to check that.')
st.write('53 dissatisfied employees have been working in the same role for 6 to 15 years. Perhaps they want and deserve a promotion but have not received one. How long have they been without a promotion? We will see next.')
st.write('A relevant fact: why are there 11 people with roles called "others"? I think this will be an interesting point to check.')
st.write('I also checked information about JOB SATISFACTION. 73% of all unsatisfied employees are not dissatisfied with their job, and 54% are highly or very highly satisfied. So, with that, we can see that the main problem is not their jobs. Obviously, we can understand why 27% are unsatisfied and try to solve this problem.')
st.write('It is also important to check if they have any conflict with their respective managers. It attracts attention that employees with 6 to 15 years with the same manager—where does dissatisfaction begin? And the portion between 0 to 5 years with the same manager—how long have these managers been in their roles? Do they have enough preparation to be leaders?')
st.write('Another significant point is our employees with 4 to 10 and 11+ years in the company who are unsatisfied. They have spent a lot of time with us. What are the reasons for this dissatisfaction? It is extremely important to know this from all unsatisfied people, but this group is special due to their time with the company.')
st.write('Now, the issue of promotion: 13 employees have gone more than 9 years without a promotion, which caught my attention. Why have not they been promoted? Are they bad employees? Or are they at the ceiling of their position? I think not all of them are at the ceiling because 4 of them earn less than 5k per month. I think this is another crucial reason people are dissatisfied.')
st.write('Other important point is relationship satisfaction. We have 33% of all unsatisfied employees with low or medium satisfaction in this area. Do we have a prepared sector to receive complaints about bullying, harassment, and humiliation? Why do not these people have good relationships with others? This is a crucial point.')

st.write('#### __Below I listed the principal points to check:')
st.write('* Conflict with Manager;')
st.write('* Monthly Income;')
st.write('* Years Without Promotion;')
st.write('* Check what is happening in Research & Development department;')
st.write('* Job Satisfaction;')
st.write('* Relationship Satisfaction')

st.markdown('### __Conclusion:')
st.write('I did this brief analysis of this topic, but it is extremely necessary for the company to carry out an anonymous survey for ALL people to respond. What points do we need to improve? If you could, what would you change about the company tomorrow? Do you have dissatisfaction? With whom? What is happening within the company and outside? Do you need support with something in your personal life?')
st.write('If our employees are healthy and happy, they will be able to work better, and our company will be better. They are important; they are the main engine. If they AND WE are not doing well or have a problem inside or outside of here, we will NOT be able to perform at the best we can.')
st.write('Comparing previous employee satisfaction data will help to identify areas of improvement and success over time. If there are no records, initiating regular feedback is extremely necessary.')
st.write('Tracking employee turnover is crucial to understand internal issues. Analysis about turnover rates by department and reasons can reveal trends. If there is no historical data, we need to start this as soon as possible.')
st.markdown('### ')