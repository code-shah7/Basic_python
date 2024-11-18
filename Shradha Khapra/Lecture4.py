# #DICTIONARY
# Info={
#     "key":"value",
#     "Name" :  "Aditya",
#     "AKA" : "shershah",
# }
# print(Info)

# Stu= {
#     "name":"Aditya",
#     "Subject":{
#         "Phy":"100",
#         "chem":"100",
#         "Math 4":100,
#     }
# }
# print(Stu["Subject"])
# print(Stu)
# print(Stu["Subject"]["chem"])







#SET
collection = {1,2,3,3,3,3,"hello","hello","hello",4}
print(collection)
print(len(collection)) #total no. of items


#Store following word meanings in a python dictionary
#table : “a piece of furniture”,“list of facts & figures”
# cat : “a small animal”

# thing={
#     "table" : ["a piece of furniture","list of facts & figures"],
#      "cat": "a small animal"
#      }
# print(thing)
# '''You are given a list of subjects for students. Assume one classroom is required for 1
#  subject. How many classrooms are needed by all students.

# ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++,“C”'''

classroom = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(classroom)
print(len(classroom))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
mark={}
math=input("Enter marks of math")
mark.update({"Math":math})
Hindi=input("Enter marks of Hindi")
mark.update({"Hindi":Hindi})
English=input("Enter marks of English")
mark.update({"English":English})

# subject = {
#     "maths" : math,
#     "hindi"   : Hindi,
#     "English" : English,
# }

print(mark)
