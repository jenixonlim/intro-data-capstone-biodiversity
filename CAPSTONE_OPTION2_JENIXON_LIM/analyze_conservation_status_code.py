Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import codecademylib
#importing matplotlib and pandas
from matplotlib import pyplot as plt
import pandas as pd

#creating species datafram from the 'species_info.csv' file
species=pd.read_csv('species_info.csv')
#getting a snapshot of the species dataframe
print species.head()

#getting the number of different species
species_count=species.scientific_name.nunique()
print species_count

#returning just the different categories 
species_type=species.category.unique()
print species_type

#returning just the different conservation statuses
conservation_statuses=species.conservation_status.unique()
print conservation_statuses

#using groupby to determine the number of species in each conservation status
conservation_counts=species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts

#this replaces the NaN in the conservations_counts data frame with 'No Intervention'
species.fillna('No Intervention', inplace = True)
#running the previous groupby again except this time with the 'No Intervention' conservation status
conservation_counts_fixed=species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts_fixed
