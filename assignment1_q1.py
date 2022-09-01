ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("The list: ")
print(ages)
ages.sort()
print("Sorted list: ")
print(ages)
minAge = min(ages)
maxAge = max(ages)
print("Minimum age: " + str(minAge));
print("Maximum age: " + str(maxAge));
ages.append(minAge)
ages.append(maxAge)
medianAge = 0
print('List after adding min and max ages: ')
print(ages)
if(len(ages)%2==0):
    middleIndex = len(ages)/2
    oneMidAge = ages[middleIndex]
    twoMidAge = ages[middleIndex+1]
    medianAge = oneMidAge + twoMidAge;
else:
    middleIndex = (len(ages)+1)/2
    medianAge = ages[middleIndex]
print("Median age: " + str(medianAge/2))
ageSum = 0
for x in ages:
    ageSum += x
print("Average age: " + str(ageSum/len(ages)))
print ("Range of age: " + str(max(ages) - min(ages)))
