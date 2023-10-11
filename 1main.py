#Packages I need
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns
import plotly.graph_objects as go
#Layout the page with headings 
header = st.container()

dataset = st.container()
features = st.container()
model_training = st.container() 

with header:
	st.title('Lego Sales Across Time')
	st.text('Adding my previous visulizations to streamlit app')

#Display our main data set
with dataset: 
	st.header('Lego Sets and Themes')
	st.text(' I found this dataset on kaggle from the previous assignemnt. It looks at lego set sales data across time. An indepth look into lego set themes, their sales numbers and also lots of techinacl data all the way down to the number of parts!')

	lego_data = pd.read_csv('Data/lego_sets_and_themes.csv')
	st.write(lego_data.head())

# Adjust the data based on the slider's value.
    # For demonstration purposes, let's say you only want to display data for years that have more sets than the max_depth value.
    filtered_data = lego_data[lego_data['year_released'].value_counts() > max_depth]
    
#Our bar plots 
	st.subheader('Quantity of Lego Sets Released Each Year')
	number_parts = pd.DataFrame(lego_data['year_released'].value_counts()).head(50)
	st.bar_chart(number_parts)




	st.subheader('Time stamp data showing each theme and the span of years for production ')
	lego_2000 = lego_data[lego_data.year_released >= 2000]
	fig_year = px.violin(
    lego_2000, 
    x="theme_name", 
    y="year_released", 
    color='theme_name'
	)

	

	st.plotly_chart(fig_year)


with features:
	st.header('Features I Created')

	st.markdown('* **First Feature:** First feature relating to lego dataset')

with model_training:
	st.header('Interactive Model')
	st.text(' Here you can choose the parameters of the model')

	sel_col, disp_col = st.columns(2)

	


	number_estimators = sel_col.selectbox('How many legos should we sell?', options = [100,200,300, 'No limit'], index = 0 )

	sel_col.text('List of themes')
	sel_col.write(lego_data.theme_name)

	input_feature = sel_col.text_input('What imformation would you like to view?', 'set_name')


	



	
