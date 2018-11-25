""" 
PSIT Data Analysis Project
"""

import pandas

def main():
    """ Get data from CSV and mannage data """
    #Mannage File
    data = pandas.read_csv('Health_AnimalBites.csv')

    #Clean data
    data_group = data.groupby(['SpeciesIDDesc']).size()
    print(data_group)

main()
