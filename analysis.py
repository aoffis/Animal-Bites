""" 
PSIT Data Analysis Project
"""

import pandas, pygal

def main():
    """ Get data from CSV and manage data """
    #Manage File from .csv >>> DataFrame(by using pandas)
    data = pandas.read_csv('Health_AnimalBites.csv')

    #Clean data
    data_group = data['SpeciesIDDesc'].value_counts()
    print(data_group)

    #Species of dog
    dog_specie = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['BreedIDDesc']).size()
    print(dog_specie)

    #Gender of dog
    dog_gen = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['GenderIDDesc']).size()
    print(dog_gen)

    #Color of dog
    dog_color = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['color']).size()
    print("---Color of Dog---", dog_color, sep="/n")

    #color of Pitbull
    pit_color = data[data['BreedIDDesc'] == 'Pit Bull'].groupby(['color']).size()
    print("---Color of Pit bull---", pit_color, sep="/n")

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



    """
    Show data in graph(by using pygal)
    """

    #Show most animal that bite people in U.S.A.(in pie chart)
    animal = data_group.sort_values(ascending=False).to_dict()
    sol = pygal.SolidGauge(half_pie=True, inner_radius=0.7)
    for i in animal:
        sol.add(i, animal[i])
    sol.title = 'Most Animal that Bite People'
    sol.render_to_file('animals.svg')
    sol.render_in_browser()

    #Show top 10 species dog(in treemap chart)
    animalz = dog_specie.sort_values(ascending=False).to_dict()
    tree = pygal.Treemap()
    for i in animalz:
        tree.add(i, animalz[i])
    tree.title = 'Species of Dogs that Bite People'
    tree.render_to_file('speciesdog.svg')
    tree.render_in_browser()

    #Show color of Dog(in horizontal bar chart)
    color_dog = dog_color.sort_values(ascending=False)[:10].to_dict()
    bar = pygal.HorizontalBar()
    bar.title = 'Top 10 colors of Dog'
    for i in color_dog:
        bar.add(i, color_dog[i])
    bar.render_to_file('top10colorsdog.svg')
    bar.render_in_browser()
    
    #Show color of Pitbull(in horizontal bar chart)
    color_pit = pit_color.sort_values(ascending=False)[:10].to_dict()
    bar_ = pygal.HorizontalBar()
    bar_.title = 'Top 10 colors of Pitbull'
    for i in color_pit:
        bar_.add(i, color_pit[i])
    bar_.render_to_file('top10colorspitbull.svg')
    bar_.render_in_browser()

    #Area
    zip_code = data[data['SpeciesIDDesc'] == 'Dog'].groupby(['victim_zip']).size().sort_values(ascending=False)

main()
