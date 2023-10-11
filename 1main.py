# Import necessary packages
import streamlit as st
import pandas as pd
import plotly.express as px

# Layout the page with headings
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

# Read the Lego dataset
lego_data = pd.read_csv('Data/lego_sets_and_themes.csv')

# Define Streamlit app
with header:
    st.title('Lego Sales Across Time')
    st.text('Adding my previous visualizations to a Streamlit app')

# Display the main dataset
with dataset:
    st.header('Lego Sets and Themes')
    st.text('I found this dataset on Kaggle from the previous assignment. It looks at Lego set sales data across time. An in-depth look into Lego set themes, their sales numbers, and also lots of technical data all the way down to the number of parts!')
    
    # Your data filtering code (you can adjust this as needed)
    max_depth = st.slider('Filter by Minimum Number of Sets in a Year', min_value=10, max_value=100, value=20, step=10)
    filtered_data = lego_data[lego_data['year_released'].value_counts() > max_depth]
    
    st.subheader('Quantity of Lego Sets Released Each Year')
    number_parts = pd.DataFrame(lego_data['year_released'].value_counts()).head(50)
    st.bar_chart(number_parts)

    st.subheader('Time stamp data showing each theme and the span of years for production')
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
    number_estimators = st.selectbox('How many Legos should we sell?', options=[100, 200, 300, 'No limit'], index=0)

    st.text('List of themes')
    st.write(lego_data.theme_name)

    input_feature = st.text_input('What information would you like to view?', 'set_name')

    # Now you can use these parameters in your model (update this part with your model code)
    # For example:
    # from sklearn.ensemble import RandomForestRegressor
    # model = RandomForestRegressor(max_depth=max_depth, n_estimators=number_estimators)
    # ...
    # Perform model training and predictions here

    # You can display model results or visualization here based on your model predictions

# Add comments and explanations as needed to make the code more understandable.
