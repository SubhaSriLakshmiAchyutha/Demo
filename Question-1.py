# input from question
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorting the ages in ascending order
ages = sorted(ages)
print("The sorted ages are", ages)

# finding the minimum and maximum ages
print("The minimum age is:", min(ages))
print("The maximum age is:", max(ages))

# adding the minimum and maximum to the list
ages.append(min(ages))
ages.append(max(ages))
print("The minimum and maximum ages are added to the list", ages)
# finding median of the ages
n = len(ages)
median = ages[n//2]
print("The median age of the list is:", median)

# print the average of ages
average = sum(ages) / len(ages)
print("The average of the list:", average)
# range of the ages
print("the range of the list is:", max(ages)-min(ages))


