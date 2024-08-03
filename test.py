import pandas as pd
import streamlit as st

@st.cache_data
def read_file():
    df = pd.read_csv('data.csv')
    df = df.rename(columns={'prod_1': 'January', 'prod_4': 'April', 'prod_7': 'July', 'prod_10': 'October'})
    df['water_depth'] = df['water_depth']*100
    return df

st.title('Welcome to test!')

df_raw = read_file()
city_list = df_raw.city.unique()
city = st.selectbox('Choose a city:', city_list)

df = df_raw[df_raw['city']==f'{city}'].drop(columns='city')
st.line_chart(df, x='water_depth', y=['January', 'April', 'July', 'October'],
              y_label='Daily productivity, kg/(m^2 day)', x_label='Water depth, cm', )

st.write(df.reset_index(drop=True))
