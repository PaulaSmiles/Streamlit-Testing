import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
import streamlit as st
import pandas as pd

# Load the CSV data
csv_file = "percentage_change.csv"
percentage_change_data = pd.read_csv(csv_file)

# Display the chart
st.line_chart(percentage_change_data)

