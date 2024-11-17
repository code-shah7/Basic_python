#LIST
#MUTABLE: Can be modified after creation.    Examples: list, dict, set.
#Immutable:Cannot be modified after creation   Examples: int, float, str, tuple.

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
print("Enter You 3 most favourite cricketer name")
a = str(input("First cricketer:"))
b = str(input("Second cricketer:"))
c = str(input("Third cricketer:"))

list=[a,b,c]
print(list)


cricketer=[]
a= input("first cricketer")
b= input("second cricketer")
c= input("third cricketer")

cricketer.append(a)
cricketer.append(b)
cricketer.append(c)

print(cricketer)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)+
List=['L','E','V','E','L']
copy_list=List.copy()
copy_list.reverse()

if(List==copy_list):
    print("Yes, It is palindrom List")
else:
    print("no, it's not a palindrome")

# WAP to count the number of students with the “A” grade in the following tuple.
#[”C”,“D”,“A”,“A”,“B”,“B”,“A”]
tup=("C","D","A","A","B","B","A")
Student=tup.count("A")
print(Student)

list=["C","D","A","A","B","B","A"]
list.sort()
print(list)