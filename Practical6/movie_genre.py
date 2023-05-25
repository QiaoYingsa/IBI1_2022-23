import matplotlib.pyplot as plt

# Input dictionary
d = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7}

# Display the dictionary
for genre, count in d.items():
    print(f'{genre}: {count}')

# Extract labels and sizes from the dictionary
labels = list(d.keys())
sizes = list(d.values())

# Plot the pie chart
explode = [0] * len(labels)  # No slice is exploded
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures a circular pie chart

# Add a title to the pie chart
plt.title("Movie Genres")

# Display the pie chart
plt.show()
