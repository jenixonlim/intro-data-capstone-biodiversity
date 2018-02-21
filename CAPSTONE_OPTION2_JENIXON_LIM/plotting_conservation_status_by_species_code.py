import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

#reading the csv file to a dataframe
species = pd.read_csv('species_info.csv')

#replacing NaN with 'No Intervention'
species.fillna('No Intervention', inplace = True)

#creating a dataframe that counts the number of species according to conservation status, this is sorted in ascending order (lowest to highest)
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')
print protection_counts

#creating the figure and defining its size
plt.figure(figsize=(10, 4))
#creating an axes object
ax = plt.subplot()
#creating the bar chart
plt.bar(range(len(protection_counts)),protection_counts.scientific_name)
#setting the tick marks and the accompanying labels
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status)
#creating the y-axis label and title
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
#displaying the bar graph
plt.show()
