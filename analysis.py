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

    #Species of dog
    dog_specie = data[data['SpeciesIDDesc'] == 'DOG'].groupby(['BreedIDDesc']).size()
    print(dog_specie)

    #Gender of dog
    dog_gen = data[data['SpeciesIDDesc'] == 'DOG'].groupby(['GenderIDDesc']).size()
    print(dog_gen)

    #Color of dog
    dog_color = data[data['SpeciesIDDesc'] == 'DOG'].groupby(['color']).size()
    print("---Color of Dog---", dog_color, sep="/n")

    #color of Pitbull
    pit_color = data[data['BreedIDDesc'] == 'PIT BULL'].groupby(['color']).size()
    print("---Color of Pit bull---", pit_color, sep="/n")

main()
