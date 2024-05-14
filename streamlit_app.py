import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
# Load the CSV data into a DataFrame
csv_file_path = "percentage_change.csv"
df = pd.read_csv(csv_file_path)

# Group the data by Category
grouped = df.groupby("Category")

# Iterate over each category
for category, group in grouped:
    st.subheader(f"Category: {category}")
    
    # Create a line chart for the current category
    for code, data in group.groupby("Code"):
        st.line_chart(data.set_index("Code")["Percentage Change"])

