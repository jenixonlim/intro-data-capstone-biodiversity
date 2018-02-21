import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)

#creating a new column called 'is_protected' that is True if the conservation status is 'No Intervention'
species['is_protected'] = species.conservation_status != 'No Intervention'

#performing a category count but grouped by 'category' and 'is_protected'
category_counts=species.groupby(['category','is_protected']).scientific_name.nunique().reset_index()
print category_counts.head(20)

#pivoting the category_counts dataframe 
category_pivot=category_counts.pivot(columns='is_protected',index='category', values='scientific_name').reset_index()

#renaming the True and False columns to 'not_protected' and 'protected'
category_pivot.columns=['category','not_protected','protected']

#creating a new column called 'percent_protected' which is the number of protected species divded by the total number of species in each category
category_pivot['percent_protected']=category_pivot.protected/(category_pivot.protected+category_pivot.not_protected)
print category_pivot
