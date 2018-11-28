""" 
PSIT Data Analysis Project
"""

import pandas
import pygal

def main():
    """ Get data from CSV and mannage data """
    #Mannage File
    data = pandas.read_csv('Health_AnimalBites.csv')
    print(data)

    #Clean data
    data_group = data['SpeciesIDDesc'].value_counts()
    print(data_group.to_dict())

    #Species of dog
    dog_specie = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['BreedIDDesc']).size().sort_values(ascending=False)
    print(dog_specie.to_dict())

    #Gender of dog
    dog_gen = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['GenderIDDesc']).size()
    print(dog_gen.to_dict())

    #Color of dog
    dog_color = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['color']).size()
    print("---Color of Dog---", dog_color.sort_values(ascending=False).to_dict(), sep="/n")

    #color of Pitbull
    pit_color = data[data['BreedIDDesc'] == 'Pit Bull'].groupby(['color']).size()
    print("---Color of Pit bull---", pit_color.sort_values(ascending=False).to_dict(), sep="/n")

    #bite_date >>> Pitbull
    date = data[data['BreedIDDesc'] == 'Pit Bull'].groupby(['bite_date']).size()
    print("---Bite date of Pit bull---", date, sep='/n')

    #pygal >>> build bar chart
    #color_dog
    color_dog = pit_color.sort_values(ascending=True).to_dict()
    bar = pygal.Bar()
    for i in color_dog:
        bar.add(i, color_dog[i])
    bar.render_to_file('wowbar.svg')
    bar.render_in_browser()
main()
