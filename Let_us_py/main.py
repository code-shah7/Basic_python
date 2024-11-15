# Variable Type and Assignment
a = 25 #type of a is inferred as int
b = 31.4 #type of a is inferred as float
c = 'hi' #type of a is inferred as str


#Type of a variable can be checked using the built-in-function type()
d = 'Jamboree'
print(type(d)) #type will be reported as str

#simple variable assignment:
f = 10
pi = 3.14
name = 'sanjay'

#Multiple variable assignment:
a = 10 ; pi = 3.14; name = 'sanjay' #use ; as statement separator
a, pi , name = 10 , 3.14 , 'sanjay'
a=b=c=d=5

#ARTHMETIC OPERATORS
# Arthmetic Operators: + - * / % // **
a = 4/2  #performs true division and yields a float 2.0
b = 7%2   # % yields remainder 1
c = 3**4  # ** yields 3 raised to 4 (exponentiation)
d = 4//3 #//yields quotient 1 after discarding fraction part

# in-placement assignment operator : += -= /= %= //= **=
a **=3 #same as a=a ** 3
b %= 10#same as b = b % 10

#precedence and associativty
#operators in decreasing order of their priority (PEMDAS):
# ()         #Parentheses
# **         #Exponentiation
# *,/,//,%   #Multiplication, Division
# +,-        #Addition, Subtraction