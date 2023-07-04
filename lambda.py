# A list of dictionaries
people = [  
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"}, 
    {"name": "Draco", "house": "Slytherin"}
]

# Defining a function which tells the sort function how to do the sorting. 
def howSort(person):
    return person["name"]
    # This 1 line function can be simplified into a lambda expression...

# Now this will sort by name. 
people.sort(key=howSort)
print(people)

#...Sorts by house using a lambda expression. 
people.sort(key=lambda person: person["house"])
print(people)

