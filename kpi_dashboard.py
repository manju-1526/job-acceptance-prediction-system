import streamlit as st

st.set_page_config(
    page_title="Job Placement Dashboard",
    layout="wide"
)

st.title("🎯 Job Placement Dashboard")
st.subheader("📊 Key Performance Indicators (KPIs)")

# First Row - 4 KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Candidates", "50,124")

with col2:
    st.metric("Placement Rate", "30.27%")

with col3:
    st.metric("Job Acceptance Rate (Proxy)", "30.27%")

with col4:
    st.metric("Average Interview Score", "66.04")

# Second Row - 3 KPIs
col5, col6, col7 = st.columns(3)

with col5:
    st.metric("Average Skills Match", "73.94%")

with col6:
    st.metric("Offer Dropout Rate", "N/A")
    st.caption("Offer dropout data not available")

with col7:
    st.metric("High-Risk Candidate Percentage", "12.42%")
    st.caption("Skills match below 60%")

# Placement Status Chart
import pandas as pd

df_chart = pd.read_csv("cleaned_placement_data.csv")

st.subheader("📊 Placement Status Distribution")

placement_counts = df_chart["status"].value_counts()

placement_counts.index = placement_counts.index.map({
    0: "Not Placed",
    1: "Placed"
})

st.bar_chart(placement_counts)

# Placement Rate by Company Tier

st.subheader("📊 Placement Rate by Company Tier")

tier_placement = (
    df_chart.groupby("company_tier")["status"]
    .mean() * 100
)

st.bar_chart(tier_placement)

# Skills Match vs Placement

st.subheader("📈 Skills Match vs Placement")

skills_placement = (
    df_chart.groupby("skills_match_level")["status"]
    .mean() * 100
)

skills_placement = skills_placement.reindex(
    ["Moderate", "High", "Very High"]
)

st.line_chart(skills_placement)

# Interview Score vs Placement Rate

st.subheader("📈 Interview Score vs Placement Rate")

df_chart["score_group"] = (df_chart["interview_score_proxy"] // 10) * 10

interview_rate = (
    df_chart.groupby("score_group")["status"].mean() * 100
)

st.line_chart(interview_rate)

# Experience vs Placement

st.subheader("📊 Experience vs Placement")

experience_rate = (
    df_chart.groupby("experience_category")["status"]
    .mean() * 100
)

st.bar_chart(experience_rate)

# High-Risk Candidate Distribution

import plotly.express as px

st.subheader("🍩 High-Risk Candidate Distribution")

risk = df_chart["skills_match_percentage"].apply(
    lambda x: "High Risk" if x < 60 else "Other Candidates"
)

fig = px.pie(
    names=risk.value_counts().index,
    values=risk.value_counts().values,
    hole=0.5
)

st.plotly_chart(fig, use_container_width=True)
