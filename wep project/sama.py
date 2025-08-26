import numpy as np
import matplotlib.pylab as plt

cetegories = ['S', 'M', 'T', 'W', 'TH','F', 'SA']
values = [25, 30, 33, 38, 22, 35, 28]

plt.bar(cetegories, values, color='pink')
plt.title("Bar plot Example")
plt.xlabel("cetegories")
plt.ylabel("values")
plt.show()