import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV from user input
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.title("Percentage Change Over Time")

    # Assuming your CSV has a 'Date' column and columns for each variable
    date_column = 'Date'
    variable_columns = df.columns.drop(date_column)

    # Melt the dataframe to long format for easier plotting
    df_melted = df.melt(id_vars=[date_column], var_name="Variable", value_name="Percentage Change")

    # Create line plot or area plot for each variable
    fig = px.line(df_melted, x=date_column, y="Percentage Change", color="Variable",
                  title="Percentage Change Over Time",
                  labels={"Percentage Change": "Percent Change", "Variable": "Variable"})
    fig.update_layout(xaxis_title="Date")

    # Show the plot
    st.plotly_chart(fig)

