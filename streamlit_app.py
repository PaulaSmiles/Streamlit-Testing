import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
import streamlit as st
import pandas as pd

# Load the CSV data into a DataFrame
csv_file_path = "percentage_change.csv"
df = pd.read_csv(csv_file_path, header=None, names=["Category", "Code", "Percentage Change"])

# Group the data by Category
grouped = df.groupby("Category")

# Iterate over each category
for category, group in grouped:
    st.subheader(f"Category: {category}")
    
    # Create a line chart for the current category
    chart_data = group.pivot_table(index=group.index, columns="Code", values="Percentage Change")
    st.line_chart(chart_data)

