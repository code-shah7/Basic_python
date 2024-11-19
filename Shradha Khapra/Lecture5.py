##LOOP
#while
'''

Print numbers from 100 to 1.
Print the multiplication table of a number n.
Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]'''


#Print numbers from 1 to 100.
# i = 1
# while i<=100:
#     i+=1
#     print(i)



#Print numbers from 100 to 1.
# i = 10
# while i>=1:
#     print(i)
#     i=i-1


#Print the multiplication table of a number n.
# a=int(input("enter any number:"))
# i=1
# while i<=10:
#       print(a*i)
#       i=i+1
 

# Print the elements of the following list using a loop:

# numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0

# while index < len(numbers):
#     print(numbers[index])
#     index += 1

# Search for a number x in this tuple using loop:
tup=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# x =int(input("Enter"))
# i=0
# while i<= len(tup):
#     if(tup[i]==x):
#         print("FOUnd" ,i)
#     else:
#         print("not found",i)
#     i+=1


##BREAK and #CONTINUE
#Break
# x=36
# i = 0
# while i < len(tup):
#      if(tup[i] == x):
#           print("found",i)
#           break
#      else:
#           print("finding..")
#           i += 1
# print("end of loop")
     


#continue
# i = 0
# while i <= 100:
#     if(i%2==0):
#          i+= 1
#          continue
#     print(i)
#     i +=1

# #     #For Loop
# list="SHERSHAH"
# for char in list :
#          print(char)
# else:
#         print("end")
#Print the elements of the follo wing list using a loop:
# lists=[1,4,9,16,25,64,81,100]
# for char in lists :
#     print(char)

#search for a number x in this tuple using loop:
# num = (1,4,9,16,25,36,49,64,81,100) 
# x = 64
# for el in num :
#     print(el)
#     if (el == x) :
#      print ("x found")
#      break
# else :
#    print("not found")/


#range
# for i in range(10):            #range(stop)
#     print(i)
# for i in range (1,10):        #range(start,stop)
#     print (i)
# for i in range (2 , 10, 2):  #range(start,stop, step)
#     print(i)

# for i in range (2 , 100, 2):
#     print (i)

# #Using for & range()
# #print numbers from 1 to 100.
# for i in range (1,101):
#     print(i)
# #print numbers from 100 to 1.
# for j in range (100,1,-1):
#     print(j)
#print the multiplication table of a number
# x=int(input("Enter num:"))
# for i in range (1,11):
#     print(x*i)

# #pass statement
# for i in range (10):
#     pass

#WAP to find the sum of first n numbers (using while)
n = 5
sum =0
for i in range (1 , n+1):
    sum +=1
print("total sum", sum)



#WAP to find the factorial of first n numbers. (usingfor)