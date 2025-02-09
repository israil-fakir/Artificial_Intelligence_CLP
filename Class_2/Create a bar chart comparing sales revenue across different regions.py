import matplotlib.pyplot as plt
import numpy as np
 
regions = ["Dhaka", "Khulna", "Chittagong", "Rajshahi", "Sylhet"]

sales_revenue = np.array([50000, 60000, 40000, 30000, 20000])

plt.bar(regions, sales_revenue, color="Green")

plt.title("Sales Revenue Across Different Regions")
plt.xlabel("Regions")
plt.ylabel("Sales Revenue")

plt.show()
