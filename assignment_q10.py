print("Input weights in LBS of all students:")
allWeights = str(input())
weights_list = allWeights.split(" ")
print("All weights received in LBS:")
print(weights_list)
weights_kg = []
for x in weights_list:
    weights_kg.append("{:.2f}".format(float(x) * 0.45359237))
print("Weight in kg: ")
print(weights_kg)
