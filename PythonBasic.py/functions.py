#Define the great function that takes a name as a parameter
def greet(name):
    return f"Hello, {name}!"

#call the greet function with a specific name and print the resutl
print(greet("Aditya")) #This will print "Hello,Aditya!"

#Take input from the user for the name
user_name = input("enter your name: ")

#Call the greet function with the user-provided name and print the result\
print(greet(user_name)) #This will print "Hello, <user_name>!"

#default params
def greet2(name, message="Hello"):
    return f"{message}, {name}!"

print(greet2("Aditya")) #This will print "hello, aditya"
    
    #variable length args

def sum_all(*numbers):
        total = 0
        for num in numbers:
            total += num
        return total

print(sum_all(1, 2, 3,)) #This will print 6 

    #keyword args
def display_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

display_info(name="Aditya", age=20)

    #return type
def get_full_name(first_name, last_name):
        full_name = f"{first_name}{last_name}"
        initials = f"{first_name[0]}{last_name[0]}"
        return full_name, initials

name, initials = get_full_name("Aditya","Shershah")
print(name) #This will print "Aditya Shershah"
print(initials)#This will print "AS"
print(get_full_name("Aditya", "Dhruv")) #this will print ("Aditya Dhruv", "AD")