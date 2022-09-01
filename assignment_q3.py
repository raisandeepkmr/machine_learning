brothers = ("pradeep", "rinku")
print("Brothers: ")
print(brothers)
sisters = ("jeena", "poonam")
print("Sisters: ")
print(sisters)
siblings = brothers + sisters
print("Siblings: ")
print(siblings)
print("Number of siblings: " + str(len(siblings)))
siblingsList = list(siblings)
siblingsList[2]="Jina"
siblings = tuple(siblingsList)
print("Modified Siblings: ")
print(siblings)

familyMembers = ("papaji", "mummuji")
familyMembers += siblings;
print("Family members: ")
print(familyMembers)