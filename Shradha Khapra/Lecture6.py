#FUNCTION
#BLOCK OF STATEMENT THAT PERFORM A SPECIFIC TASK.

'''def func_name(parameter1,parameter2..):
           some work
           return val'''

'''func_name(arguments1,arguments2...)#function call'''

# def calcSum(a,b):
#     sum=a +b
#     print(sum)
#     return

# calcSum(2,30)
# calcSum(100,499)


# #Function defination
# def calcSum(a, b):   #parameter
#     return a +b

# #function call
# sum = calcSum(1902,842)  #argument
# print(sum)

def printHello():
    print("hello")

printHello()
printHello()
printHello()
printHello()
printHello()

#average of 3 numbers
def avg_three(a,b,c):
    avg=((a+b+c)/3)
    print(avg)
    return

# avg_three(2,2,2)

#WAF to print the length of a list. (list is the parameter)

def len_list(a):
    print(len(a))
    return a

list=[1,2,3,4,5,6]
len_list(list , )

# #WAF to print the elements of a list in a single line. (list in the parameter)

def el_list(a):
    for el in a:
     print(el , end =" ")
    return
a=[1,2,3,4,5,6,7,8,9,10]
el_list(a)

#WAF to find the factorial of n . (n is the parameter)
def calfact(n):
   fact =1 
   for i in range (1, n+1):
     fact  *=i
     print(fact)

calfact(5)


#WAF to convert usd to inr
def currency_convert(a):
       inr=a*83
       print(inr)
       return

currency_convert(50)

#rucursive Function
def show(n):
    if(n == 0):    #Base case
        return
    print(n)
    show(n-1)
show(5)

def fact(n):
    if(n == 0 or n ==1):
        return 1
    else:
        return fact(n-1) * n 
    
print(fact(6))

#WA recursive function to calculate the sum of first n natural numbers.

def natural(n):
    if ( n==0):
        return
        print(n)
    natural(n-1)+n 
natural(6)

#write a recursive function to print all elements in a list.