#Description: This file demonstrates the use pf variables in python.
name = "Aditya"
age = 20
is_number = True

print ("hello, my name is "+ name + ' and I am ' + str(age)+'years old.')

#integer
count = 100 
print (count)

#float int (point/decimal)
pi = 3.14
print (pi)

#complex Number
complex_num = 2+3j
print (complex_num)

#operations
total = count + 50
radius = int(input("Enter Radius = 5"));
area = pi * radius ** 2
print (total)
print (area)

#string
single_qoute_str = 'Namaste'
double_qoute_str = "Hello"
multi_line_str = """This is a Multi-line string."""
print(single_qoute_str)
print(double_qoute_str)
print(multi_line_str)

#string conactenation
greeting = single_qoute_str + " " + double_qoute_str
print(greeting)

#string formating
name = "Aditya"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)

#string methods
uppercase_name = name.upper()
print (uppercase_name)

#boolean
is_active = True
is_admin = False
can_access = is_active and is_admin
print (can_access)