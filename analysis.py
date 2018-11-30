""" 
PSIT Data Analysis Project
"""

import pandas
import pygal

def main():
    """ Get data from CSV and manage data """
    #Manage File from .csv >>> DataFrame(by using pandas)
    data = pandas.read_csv('Health_AnimalBites.csv')

    #Sort most animal that bite people in U.S.A.
    data_group = data['SpeciesIDDesc'].value_counts()
    print(data_group.to_dict())

    #Sort species of dog
    dog_specie = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['BreedIDDesc']).size().sort_values(ascending=False)
    print(dog_specie.to_dict())

    #Sort gender of dog
    dog_gen = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['GenderIDDesc']).size()
    print(dog_gen.to_dict())

    #Sort color of dog
    dog_color = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['color']).size()
    print("---Color of Dog---", dog_color.sort_values(ascending=False).to_dict(), sep="/n")

    #Sort color of Pitbull
    pit_color = data[data['BreedIDDesc'] == 'Pit Bull'].groupby(['color']).size()
    print("---Color of Pit bull---", pit_color.sort_values(ascending=False).to_dict(), sep="/n")

    #Sort Bite date of Pitbull
    date = data[data['BreedIDDesc'] == 'Pit Bull'].groupby(['bite_date']).size()
    print("---Bite date of Pit bull---", date, sep='/n')

    #Show data in graph(by using pygal)
    #Show most animal that bite people in U.S.A.(in pie chart)
    animal = data_group.sort_values(ascending=False).to_dict()
    pie = pygal.Pie()
    for i in animal:
        pie.add(i, animal[i])
    pie.title = 'Most Animal that Bite People'
    pie.render_to_file('wowpie.svg')
    pie.render_in_browser()
    
    #Show color of Pitbull(in bar chart)
    color_dog = pit_color.sort_values(ascending=False).to_dict()
    bar = pygal.Bar()
    for i in color_dog:
        bar.add(i, color_dog[i])
    bar.title = 'Most color of Pitbull'
    bar.render_to_file('wowbar.svg')
    bar.render_in_browser()
main()
