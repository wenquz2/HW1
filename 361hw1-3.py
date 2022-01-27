import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import scipy.stats as stats

#part(a)
df = pd.read_csv("nuclear-plants.csv")
df = df.filter(['Mwatts', 'Cost'])
#print(df.corr())

plt.figure(figsize=(8,8))
plt.scatter(df['Mwatts'], df['Cost'])
plt.xlabel("Mwatts")
plt.ylabel("Cost")
plt.title("Scatter plot of Cost vs. Mwatts")
#plt.show()

#part (b)
cost = df['Cost']
print("the mean cost of a power plant is" )
print(cost.mean())
print("the standard deviation of the costs of the power plant is", cost.std(ddof = 0) )

#part(c)
power = df["Mwatts"]
cost_per_megawatt = cost/power
print("the mean cost per megawatt is", cost_per_megawatt.mean())
print("the standard deviation of cost per megawatt is", cost_per_megawatt.std(ddof = 0))
print("the median of cost per megawatt is", cost_per_megawatt.median())

#part(d) bins = len(num_cpm)
num_cpm = cost_per_megawatt.value_counts()
plt.subplot(1,2,1)
plt.hist(cost_per_megawatt, bins = len(num_cpm))
plt.xlabel("")
plt.ylabel("")
plt.title("Histogram of the cost per megawatt")
plt.show()