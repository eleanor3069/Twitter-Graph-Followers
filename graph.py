# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import config
 
# Build a dataframe with 4 connections
df = pd.read_csv("./test_data.csv")
df
 
# Build your graph
G=nx.from_pandas_edgelist(df, 'screen_name', 'follower')
 
# Plot it
nx.draw(G, with_labels=True)
plt.show()