# #Easy coding Question
# '''convert m to km '''


# m=int(input("Enter your Distance in Meter:"))
# def distance_converter(m):
#     km=m/1000
#     print("M to Km:",km ,'km')
#     return

# distance_converter(m)



# m=int(input("Enter your Distance in Meter:"))
# km = m/1000

# print("Given Meter distance in Km:", km  ,'km')

# # '''Calculate Simple Interest'''

# p=int(input("Enter your principal amount :"))
# r=float(input("Enter you rate (per annum):"))
# t=float(input("Enter your Time (in years):"))

# def simple_interest(p,r,t):
#     simpleInterest=(p*r*t)/100
#     print("simple interest :  ",simpleInterest,"₹")
#     return

# simple_interest(68000,50/3,3/4)
# simple_interest(p,r,t)

# '''Find largest number in list'''
# #num=[10,20,30,40,50,100]

# '''Check number if prime or not'''
def check_prime(prime):
    if prime%prime==0 and prime%1==0:
        print("it's a prime number:",prime)
    else:
        print("No it is not a prime number:",prime)

        return
    
check_prime(6)
