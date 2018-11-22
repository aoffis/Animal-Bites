import csv
from itertools import groupby

#Mannage File
file = open('Health_AnimalBites.csv')
data = csv.reader(file)
table = [row for row in data]

#Clean data
gb_animal = groupby(table, lambda x: x[1])
all_animal = dict()

#How many animal that bite people
for animal in gb_animal:
    if animal[0] not in all_animal:
        all_animal[animal[0]] = 1
    else:
        all_animal[animal[0]] += 1

print(all_animal)