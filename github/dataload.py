import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt


st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# 데이터 불러오기
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# 텍스트 요소 생성. 사용자에게 데이터가 로드 되고 있음을 알린다.
data_load_state = st.text('Loading data...')

# 10000개의 행의 데이터를 로드한다.
data = load_data(10000)

# 데이터가 성공적으로 로드 되었음을 알린다.
data_load_state.text('Loading data...done!')

# 부제목 만들기
st.subheader('Raw data')
st.write(data)

# 픽업 위치를 맵에 표시하기
st.subheader('Map of all pickups')
st.map(data)

# 시간대별 픽업 수를 바차트로 표시하기
st.subheader('Number of pickups by hour')

# 시간대별 데이터 그룹화
data['hour'] = data[DATE_COLUMN].dt.hour
hist_values = data['hour'].value_counts().sort_index()

# 바차트 그리기
st.bar_chart(hist_values)

# PyDeck을 사용하여 위치 시각화하기
st.subheader('Pickup locations on a map')
midpoint = (np.average(data['lat']), np.average(data['lon']))

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=midpoint[0],
        longitude=midpoint[1],
        zoom=10,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=data,
            get_position='[lon, lat]',
            radius=100,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
))
