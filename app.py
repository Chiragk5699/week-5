import streamlit as st
import pandas as pd
from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write("""
# Titanic Visualization 1
""")

st.write(
    "Did women in first class have higher survival rates than men across all age groups?"
)

fig1 = visualize_demographic(df)
st.plotly_chart(fig1, use_container_width=True)

st.write("""
# Titanic Visualization 2
""")

fig2 = visualize_families(df)
st.plotly_chart(fig2, use_container_width=True)

st.write("""
# Titanic Visualization Bonus
""")

fig3 = visualize_family_size(df)
st.plotly_chart(fig3, use_container_width=True)




st.write("### Question:")
st.write(
    "Does family size affect ticket fare differently across passenger classes?"
)
from apputil import family_groups, last_names, visualize_families
st.subheader("Family Size and Fare Analysis")

table = family_groups(df)
st.dataframe(table)
st.subheader("Last Name Counts")

name_counts = last_names(df)
st.write(name_counts.head(20))
fig = visualize_families(df)
st.plotly_chart(fig)