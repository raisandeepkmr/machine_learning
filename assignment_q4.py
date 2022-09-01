it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Total IT Companies: ")
print(len(it_companies))
it_companies.add("Twitter")
print("Added 1 to IT Companies: ")
print(it_companies)
newCompanies = ["Accenture", "TCS", "Infosys"]
it_companies.update(newCompanies)
print("New IT Companies: ")
print(it_companies)
it_companies.remove("TCS")
print("After removed IT Companies: ")
print(it_companies)
'''
The built-in method, remove() in Python, removes the element from the set only if the element is present in the set,
So does the discard() method but If the element is not present in the set, then an error or exception is raised.
'''
aAndb = A.union(B)
print("A and B union")
print(aAndb)
aInterb = A.intersection(B)
print("A and B intersection")
print(aInterb)
print("Is A subset of B")
print(A.issubset(B))
print("Are A and B disjoint sets")
print(A.isdisjoint(B))
aWithb = A.union(B)
print("A with B union")
print(aWithb)
bWitha = B.union(A)
print("B with A union")
print(bWitha)
print("Symmetric difference")
print(A.symmetric_difference(B))
A.clear()
B.clear()
print("A :")
print(A)
print("B :")
print(B)
setAges = set(age)
print("Length of age:")
print(len(age))
print("Length of age-set:")
print(len(setAges))
'''The length is reduced because Set does not allow duplicates'''
