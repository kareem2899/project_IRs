import streamlit as st
import pandas as pd
import pickle

df=pickle.load(open('df.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


#webapp
def Recommendation(title):
    idx=df[df['Title']==title].index[0]
    idx=df.index.get_loc(idx)
    distances=sorted(list(enumerate(similarity[idx])),reverse=True, key=lambda x:x[1])[1:20]
    
    job=[]
    for i in distances:
        job.append(df.iloc[i[0]].Title)
    return job
st.title('Job Recommendation system Galala university')
#photo
header_image = "download.png"  
st.image(header_image, use_container_width=True)
title=st.selectbox('find similar jobs',df['Title'])

jobs=Recommendation(title)
if jobs:
    st.write(jobs) 

# Footer with contact information
footer = """
<div style="background-color: black; padding: 10px; text-align: center;">
    <h3>Contact Information</h3>
    <p>Email: kareem.mamdouhk42@gmail.com</p>
    <p>Email: maramelbana@gamil.com</p>
    <p>Super:Dr Samy |TA: Ahmed Nabil</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
