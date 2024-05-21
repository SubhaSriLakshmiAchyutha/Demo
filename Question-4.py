

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
count = len(it_companies)
print(f"length of it_companies: ", count)                  #Printing the length of companies

it_companies.add("twitter")                                 #add twitter to the it_companies Set

print(f"add new company: ", it_companies)
it_companies.update(['Walmart', 'Accenture', 'BOFA'])  # multiple it companies
print(f"updated it companies:", it_companies)   

it_companies.remove('Accenture')                           #remove one company(which raises error)
print(f"remove it companies:", it_companies)

it_companies.discard('infosys')                           #discard which doesnt raise an error
print(f"discard it companies:", it_companies)

print(f"join A union B:{A | B}")                          # Printing the Union of A and B
print(f"join A intersection B:{A & B}")                   # Printing the intersection of A and B
print(f"if A is subset of B:{A.issubset(B)}")             #Printing the subset of B 
print(f"if A is disjoint of B:{A.isdisjoint(B)}")         #printng the disjoint of B

A.update(B)                                               #joint A with B and B with A
print(A) 
B.update(A)
print(B)

print(f"symmetric difference:{A.symmetric_difference(B)}") #Printing the symmetric difference
A.clear()
B.clear()
print(f"deleting both A and B: ", A.clear(), B.clear())    #Printing the deleted set 
print(f"The length of the list age:{len(age)}")
AgeSet=set(age)                                            #convert age to set and compare length of list and set
print(f"The length of the set age:{len(age)}")


