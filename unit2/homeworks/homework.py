import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('vgsales.csv')
df.head()
Var=df["EU_Sales"]
Var
Var.mean()
Var.median()
Var.mode()
Var.var()
Var.std()
plt.scatter(df.index,Var)
plt.hist(Var)
plt.boxplot(Var)
