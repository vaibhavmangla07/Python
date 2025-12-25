import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Hello Streamlit!")

# Display a simple text
st.write("This is a Simple Text.")

# Create a DataFrame
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})

# Display the DataFrame
st.write("Here is a simple DataFrame:")
st.dataframe(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
