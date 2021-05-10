import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as date

dateStart = date.datetime.now() - date.timedelta(days=2*365)
dateToday = date.datetime.now().strftime("%Y-%m-%d")
# Pick ticker symbol of our stock
tkr_str = 'DOGE-EUR'
tkr = yf.Ticker(tkr_str)

graph  =  tkr.history(start=dateStart,end=dateToday)
graph.head()
graph = graph.reset_index()
fig = px.line(graph, x="Date", y="Open", title='Doge Price Tracker')
fig.show()
