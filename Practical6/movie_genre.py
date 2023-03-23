d = {'Comedy' :73, 'Action' :42, 'Romance' :38, 'Fantasy' :28, 'Science-fiction' :22, 'Horror' :19, 'Crime' :18, 'Documentary' :12, 'History' :8, 'War' :7 }
#make a dictionary
print(d)
#import matplotlib database
import matplotlib.pyplot as plt
#set the labels and sizes of each part
labels = 'Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horror', 'Crime', 'Documentary', 'History', 'War'
sizes = [27.3, 15.7, 14.2, 10.5, 8.2, 7.1, 6.7, 4.5, 3.0, 2.7]
#set the interval
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#set and show the pie chart
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()