import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_table('dataset/trace1.txt',header=None,low_memory=False)
print(df.tail())
x = df.iloc[0:1000,[2, 3]].values
plt.scatter(x[:500,0],x[:500,1],color='red',marker='o')
plt.scatter(x[500:1000,0],x[500:1000,1],color='blue',marker='x')
plt.show()
