# # # str1= 'Aditya '
# # # str2="Shukla"
# # # print(str1+" "+str2)     #concatenation sum of two str 
# # # str3='''Success is not final, failure is not fatal: It is the courage to continue that counts.'''
# # # print(len(str3))

# # # #Escape Character 
# # # # (\n) = for next line 
# # # # (\t) = tab space b/w two word
# # # str4="Hello My name is Aditya .\n I'm 19 year old"
# # # str4="Hello My name is Aditya. \t  I'm 19 year old"
# # # print(str4)

# # # #INDEXING

# # str = "ASD#SHERSHAH"
# # ch = str[0]
# # print(ch)
# # ch1 = str[1]
# # print(ch1)
# # ch2 = str[2]
# # print(ch2)

# # #SLICING
# # # str[ Starting_index : ending_index] #ending index is not included

# # str ="ASD%SHERSHAH"
# # print(str[4:12])
# # print(str[4:len(str)])
# # print(str[4:])            #[5:len(str)]
# # print(str[:12])           #[0:12]

# # #negative Slicing
# # print(str[-12:-1])

# # #STRING FUNCTION
# # str='i am studying python from myself'
# # str = str.capitalize()
# # print(str)

# # str='i am studying python from myself'
# # print(str.replace("python","java"))

# # str='i am studying python from myself'
# # print(str.find("python"))

# # str='i am studying python from myself'
# # print(str.count("i"))

# # #WAP to input user's first name & print its length.
# # Name = str(input("Enter your first name:"))
# # print(Name)
# # # print(len(Name))

# # WAP to find the occurence of '$' in a string.

# # Str=("price of 1 $$$$$ =80 ruppees")
# # print(Str.count("$"))



# #CONDITION STATEMENTS
# #if-elif-else(SYNTAX)

# light = input("Enter light clr:")

# if(light == "red"):
#     print("stop")
# elif(light == 'green'):
#     print("Go")
# if(light == "Yellow"):
#     print("look")
# else:
#     print("light is not working")

# # Indentation refers to the spaces or tabs used at the beginning of a line of code to define its scope or block structure.  

# #WAP to check if a number entered by the user is odd or even.

# num= int(input("Enter your number:"))

# if(num%2==0):
#     print("Number = Even")
# else:
#     print("Number is Odd")

# WAP to find the greatest of 3 numbers entered by the user.
# num1 = int(input("First num:"))
# num2 = int(input("Second num:"))
# num3 = int(input("Third num:"))

# if num1 >= num2 and num1 >= num3:
#     greatest = num1
# elif num2 >= num1 and num2 >= num3:
#     greatest = num2
# else:
#     greatest = num3

# # Displaying the result
# print(f"The greatest number is: {greatest}")

#WAP to check if a number is a multiple of 7 or not.

num = int(input("Enter Number:"))
if(num%7==0):
    print("It is multiple of 7")
else:
    print("no, it is not multiple of 7")
