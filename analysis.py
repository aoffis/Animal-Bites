""" 
PSIT Data Analysis Project
"""

import pandas

def main():
    """ Get data from CSV and mannage data """
    #Mannage File
    data = pandas.read_csv('Health_AnimalBites.csv')
    print(data)

    #Clean data
    data_group = data['SpeciesIDDesc'].value_counts()
    print(data_group)

    #Species of dog
    dog_specie = data[data['SpeciesIDDesc'] == 'DOG'].groupby(['BreedIDDesc']).size().sort_values(ascending=False)
    print(dog_specie)

    #Gender of dog
    dog_gen = data[data['SpeciesIDDesc'] == 'DOG'].groupby(['GenderIDDesc']).size()
    print(dog_gen)

    #Color of dog
    dog_color = data[data['SpeciesIDDesc'] == 'DOG'].groupby(['color']).size()
    print("---Color of Dog---", dog_color.sort_values(ascending=False), sep="/n")

    #color of Pitbull
    pit_color = data[data['BreedIDDesc'] == 'PIT BULL'].groupby(['color']).size()
    print("---Color of Pit bull---", pit_color.sort_values(ascending=False), sep="/n")

    #bite_date >>> Pitbull
    date = data[data['BreedIDDesc'] == 'PIT BULL'].groupby(['bite_date']).size()
    print("---Bite date of Pit bull---", date, sep='/n')
main()
