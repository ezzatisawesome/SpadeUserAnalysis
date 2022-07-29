import json
import matplotlib.pylab as plt

# Import file
f = open('summary.json')
data = json.load(f)

v = list(data.values())
k = list(data.keys())

fig1, ax1 = plt.subplots()
ax1.pie(v, labels=k, autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
