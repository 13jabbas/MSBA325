# Import necessary packages
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Define separate sections of the Streamlit app
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

# Read the Lego dataset from a CSV file

import os
import pandas as pd

# Get the absolute path to the CSV file
file_path = os.path.join(os.path.dirname(__file__), 'Data', 'lego_sets_and_themes.csv')

# Read the CSV file

lego_data = pd.read_csv('lego_sets_and_themes.csv')
# Define Streamlit app
with header:
    st.title('Lego Sales Across Time')
    st.text('Adding my previous visualizations to a Streamlit app')

# Display the main dataset
with dataset:
    st.header('Lego Sets and Themes')
    st.text('I found this dataset on Kaggle from the previous assignment. It looks at Lego set sales data across time. An in-depth look into Lego set themes, their sales numbers, and also lots of technical data all the way down to the number of parts.')

    # Data filtering code for selecting years with a minimum number of sets
    max_depth = st.slider('Filter by Minimum Number of Sets in a Year', min_value=10, max_value=100, value=20, step=10)
    filtered_data = lego_data[lego_data['year_released'].value_counts() > max_depth]
    
    # Display a bar chart showing the quantity of Lego sets released each year
    st.subheader('Quantity of Lego Sets Released Each Year')
    number_parts = pd.DataFrame(lego_data['year_released'].value_counts()).head(50)
    st.bar_chart(number_parts)

    # Display a violin plot showing the span of years for production of each theme
    lego_2000 = lego_data[lego_data.year_released >= 2000]
    fig_year = px.violin(
        lego_2000,
        x="theme_name",
        y="year_released",
        color='theme_name'
    )
    st.plotly_chart(fig_year)

# Features section
with features:
    st.header('Features I Created')
    st.markdown('* **First Feature:** First feature relating to Lego dataset')

# Model training section
with model_training:
    st.header('Interactive Model')
    st.text('Here you can choose the parameters of the model')

    # Define your model parameters
    max_depth = st.slider('What is your maximum depth of the model?', min_value=10, max_value=100, value=20, step=10)

    # Create a simple linear regression model
    model = LinearRegression()

    # Split the data into features and target (replace with actual features and target variable)
    X = lego_data[['feature1', 'feature2']]
    y = lego_data['target']

    # Train the model
    model.fit(X, y)

    # Make predictions
    predictions = model.predict(X)

    # Calculate model performance metrics
    mse = mean_squared_error(y, predictions)
    r2 = r2_score(y, predictions)

    # Display model results
    st.subheader('Model Predictions')
    st.write(predictions)

    st.subheader('Model Performance Metrics')
    st.write(f'Mean Squared Error: {mse:.2f}')
    st.write(f'R-squared: {r2:.2f}')
