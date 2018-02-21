import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

#loading the csv file into the observations dataframe
observations=pd.read_csv('observations.csv')
print observations.head()

#creating a new column called 'is_sheep' that uses a lambda function to make 'is_sheep' True if 'common_names' contains 'Sheep', otherwise it'll be False
species['is_sheep']=species.apply(lambda row: True if 'Sheep' in row['common_names'] else False,axis=1)

#selecting the rows of species where 'is_sheep' is True
species_is_sheep=species[species.is_sheep==True]
print species_is_sheep
#the above actually includes a lot of plants where the common name includes sheep
#we thus select the rows where is_sheep is True and the category is mammal below:
sheep_species=species_is_sheep[species_is_sheep.category=='Mammal']
print sheep_species

#merging sheep_species and observations to get a dataframe called sheep_observations
sheep_observations=pd.merge(sheep_species,observations)
print sheep_observations.head()

#Using groupby, the following shows the total sheep sightings across the three sheep species at each national park
obs_by_park=sheep_observations.groupby('park_name').observations.sum().reset_index()
print obs_by_park

#creating the figure and defining its size
plt.figure(figsize=(16,4))
#creating the axes object
ax=plt.subplot()
#creating the bar chart
plt.bar(range(len(obs_by_park)),obs_by_park.observations)
#creating the x ticks and respective labels
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name)
#creating the y-axis label and title
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
#displaying the bar chart
plt.show()
