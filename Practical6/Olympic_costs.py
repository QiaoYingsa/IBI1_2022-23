#print the sorted values
costs=[1,8,15,7,5,14,43,40]
sorted_values=sorted(costs)
print("sorted values:",sorted_values)

#prepare the database
import numpy as np
import matplotlib.pyplot as plt

# Set the data of cities and costs
cities = ['Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012']
costs = [1,8,2,7,5,14,43,40]

# Sort the data
inds = np.argsort(costs)
sortedcities = np.array(cities)[inds]
sortedcosts = np.array(costs)[inds]

# Create a bar plot
plt.bar(sortedcities, sortedcosts)

# Set the rotation of the x-axis ticks
plt.xticks(rotation=90)

# Set the labels and title
plt.xlabel("Cities")
plt.ylabel("Costs")
plt.title("Olympic Games Costs")

# Show the plot
plt.show()