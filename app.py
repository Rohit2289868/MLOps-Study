import streamlit as st

st.header("MLOps")

st.sidebar.title("MLOps Topics")
ml = st.sidebar.button("Machine Learning")
dl = st.sidebar.button("Deep Learning")
aws = st.sidebar.button("AWS")
ds = st.sidebar.button("Data Science")

if ml:
    st.header("Machine Learning")
    st.subheader("Course Syllabus")
    st.write("""
        - Introduction to Machine Learning
        - Supervised Learning
        - Unsupervised Learning
        - Reinforcement Learning
        - Feature Engineering
        - Model Evaluation and Selection
        - Deployment of Machine Learning Models
        """)
    st.subheader("Course Price")
    st.write("₹5000")

