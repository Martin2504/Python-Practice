name = "Harry"
print(name[0])      # Fetch the 1st character of the string. 

coordinate = (10.0, 20.0)   # A touple.

names = ["Harry", "Ron", "Hermione"]    # A list. 
print(names)
print(names[2])     # Fetch the 3rd element of the list. 

names.append("Draco")   # Adding to the list. 
names.sort()            # Sort the list in alphabetical order. 
print(names)

s = set()   # Created an empty set.
s.add(1)    # Add to a set.
s.add(2)
s.add(3)
s.add(2)    # Wont appear because a set is uniquie values. 

s.remove(1) # Remove from a set.

print(s)
print(f"The set has {len(s)} elements")




