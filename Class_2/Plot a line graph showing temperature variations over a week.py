import matplotlib.pyplot as plt
import numpy as np
xp = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

yp = np.array([24,26,31,33,32,33,34,30,27,25,23,21])

plt.title("Average Temperature")
plt.ylabel("Temperature")
plt.xlabel("Months")
plt.plot(xp,yp)
plt.show()