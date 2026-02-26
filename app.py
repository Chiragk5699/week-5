import streamlit as st
import pandas as pd

from apputil import (
    survival_demographics,
    visualize_demographic,
    family_groups,
    last_names,
    visualize_families
)

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# ---------------------------------------------------
# Page Setup
# ---------------------------------------------------
st.set_page_config(page_title="Titanic Analysis App", layout="wide")

st.title("🚢 Titanic Data Analysis App")


# ===================================================
# ================= EXERCISE 1 ======================
# ===================================================

st.header("Exercise 1: Survival Demographics")

st.write(
    """
    **Question:**  
    How does survival rate differ across passenger class,
    sex, and age group?
    """
)

# Call function (NO df argument)
survival_table = survival_demographics()

st.subheader("Survival Demographics Table")
st.dataframe(survival_table)

fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)


# ===================================================
# ================= EXERCISE 2 ======================
# ===================================================

st.header("Exercise 2: Family Size and Wealth")

st.write(
    """
    **Question:**  
    Does family size influence ticket fare differently
    across passenger classes?
    """
)

# ---------------------------------------------------
# Family Groups Table
# ---------------------------------------------------

family_table = family_groups()

st.subheader("Family Size Grouped by Passenger Class")
st.dataframe(family_table)
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)


# ---------------------------------------------------
# Last Name Counts
# ---------------------------------------------------

st.subheader("Last Name Counts")

name_counts = last_names()

st.write(name_counts.head(20))

st.write(
    """
    **Insight:**  
    Many large last-name groups align with larger family sizes,
    but not perfectly. Some passengers share last names without
    being recorded in the same immediate family group.
    """
)


# ---------------------------------------------------
# Visualization
# ---------------------------------------------------

st.subheader("Visualization: Average Fare by Family Size and Class")

