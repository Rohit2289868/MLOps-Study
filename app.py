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

if dl:
    st.header("Deep Learning")
    st.subheader("Course Syllabus")
    st.write("""
        - Introduction to Deep Learning
        - Neural Networks
        - Convolutional Neural Networks (CNN)
        - Recurrent Neural Networks (RNN)
        - Long Short-Term Memory (LSTM)
        - Generative Adversarial Networks (GAN)
        - Deep Learning Model Deployment
        """)
    st.subheader("Course Price")
    st.write("₹7000")

if aws:
    st.header("AWS")
    st.subheader("Course Syllabus")
    st.write("""
        - Introduction to AWS
        - AWS Cloud Services
        - AWS Machine Learning Services
        - Setting Up AWS Environment
        - Building and Deploying Models on AWS
        - Monitoring and Managing Models on AWS
        """)
    st.subheader("Course Price")
    st.write("₹6000")

