import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf
import csv

st.markdown("<h1 style='text-align: center; color: #4C4C6D;'>Stock Comparison 🌱</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; font-weight: lighter; color: #916BBF;'><i><a style='text-decoration: none; color: #1E3163;' target='_blank' href='https://twitter.com/hoodie_coder'>Nodebanker ⚡️</a></i></h4>", unsafe_allow_html=True)
st.write(" ")
file = open('tickers.csv')
tickers = pd.read_csv(file)

dropdown = st.multiselect("Pick Stock Ticker(s):", tickers)

start = st.date_input('Select Start', value = pd.to_datetime('2021-01-01'))
end = st.date_input('Select End', value = pd.to_datetime('today'))


def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    closingPrice = yf.download(dropdown,start,end)['Adj Close']
    stock_returns = relativeret(yf.download(dropdown,start,end)['Adj Close'])
 
    volume = yf.download(dropdown,start,end)['Volume']
   
 
    st.write("### Closing Price")
    st.line_chart(closingPrice)
    st.write("### Returns")
    st.area_chart(stock_returns)
    st.write("### Volume")
    st.bar_chart(volume)
  


