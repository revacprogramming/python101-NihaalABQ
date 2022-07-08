$ pip install pandas
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("dataset0.csv")
df.plot()
df.plot(kind='scatter',x='x',y='y')
df.plot(kind='density')
