# creating a tuple of my sisters and brothers
brother_names = ('Srinu', 'Ganesh')
sister_names = ('Lohitha' , 'Monika')
print(brother_names)
print(sister_names)

# Joining the both tuples to siblings
siblings = brother_names+sister_names
print(siblings)

# Number of siblings
a = len(siblings)
print("The number of siblings are;", a)

# Modifying tuple and adding my parents names
family_members = siblings +('KalikiMurthy' , 'AnanthaLakshmi')
print("Family members are:" , family_members)
