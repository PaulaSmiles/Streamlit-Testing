import streamlit as st

st.write('Hello world!')


import requests
import plotly.express as px
import pandas as pd

# Make the API request
response = requests.get("https://api.census.gov/data/2024/cps/basic/mar?get=PEMLR,PWSSWGT,PEMARITL&CBSA=12940&key=4e50aa76776515ce3bd4ec198d3d0d7d97f9b2fa")

# Check if the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()

    # Dictionary to map PEMLR codes to descriptions
    PEMLR_descriptions = {
        "1": "Employed-At Work",
        "2": "Employed-Absent",
        "3": "Unemployed-On Layoff",
        "4": "Unemployed-Looking",
        "5": "Retired-Not In Labor Force",
        "6": "Disabled-Not In Labor Force",
        "7": "Other-Not In Labor Force",
        "-1": "Not in Universe"
    }

    # Initialize variables to store aggregated values
    total_PEMLR_counts = {description: 0 for description in PEMLR_descriptions.values()}

    # Iterate over the data rows (skip the header row)
    for row in data[1:]:
        # Extract values from the row
        PEMLR_code = row[0]

        # Increment the count for the corresponding PEMLR description
        if PEMLR_code in PEMLR_descriptions:
            total_PEMLR_counts[PEMLR_descriptions[PEMLR_code]] += 1

    # Convert the aggregated counts to a DataFrame for Plotly Express
    df = pd.DataFrame(list(total_PEMLR_counts.items()), columns=['PEMLR', 'Count'])

    # Create the bar graph using Plotly Express
    fig = px.bar(df, x='PEMLR', y='Count', title='PEMLR Counts')
    fig.show()

else:
    print("Failed to retrieve data.")
