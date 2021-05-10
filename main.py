import yfinance as yf
import plotly.express as px
import datetime as date



tkr_str = 'DOGE-EUR'
tkr = yf.Ticker(tkr_str)
dateStart = date.datetime.now() - date.timedelta(days=1*365)
dateToday = date.datetime.now().strftime("%Y-%m-%d")
graph  =  tkr.history(start=dateStart,end=dateToday,interval="1h")


graph.head()
graph = graph.reset_index()
fig = px.line(graph, x="index", y="Open", title='Doge Price Tracker')
fig.show()
