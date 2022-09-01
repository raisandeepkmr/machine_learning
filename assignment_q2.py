dog = {}
dog.update({"name":""})
dog.update({"color":""})
dog.update({"breed":""})
dog.update({"legs":""})
dog.update({"age": 0})
print("Dog dictionary: ")
print(dog)

student = {}
student["first_name"]=""
student["last_name"]=""
student["gender"]=""
student["age"]=0
student["marital_status"]=""
student["skills"]=[]
student["country"]=""
student["city"]=""
student["address"]=""
print("Length of student: " + str(len(student)))

skills = student["skills"]
print("Type of skills: ")
print(type(skills))

student["skills"].append("java")
student["skills"].append("python")
print("New Skills: ")
print(student["skills"])

print("Student Keys: ")
print(student.keys())
print("Student Values: ")
print(student.values())