import pandas as pd

import streamlit as st
st.set_page_config(
    page_title="Job Acceptance Prediction System",
    layout="wide"
)

st.title("🎯 Job Acceptance Prediction System")
st.write("HR Analytics and Machine Learning Dashboard")

st.subheader("Machine Learning Model Comparison")

ml_results = pd.read_csv("ml_results.csv")

st.dataframe(ml_results, use_container_width=True)

st.bar_chart(
    ml_results.set_index("Model")["Accuracy"]
)
