#file I/O
#read

# f=open("C:\Learning\Backend\Python\Shradha Khapra\About.txt",  "r")
# data = f.read(10)
# print(data)
# print(type(data))
# f.close()

#Write
f=open("C:\Learning\Backend\Python\Shradha Khapra\About.txt",  "a")
f.write("\ni complete this lecture today ")
f.close()


#With Syntax
with open("demo.txt","a") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("new data") 


#Deleting a file

import os
os.remove("filename")