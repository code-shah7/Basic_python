#Define variables for comparison operations
a = 10
b = 20

#comparison operations
equal_to = (a==b) #Equal to 
not_equal_to = (a != b) # Not Equal to 
greater_than = (a > b) #greater than 
less_than = (a < b) # Less than 

#print results
print(f"a == b : {equal_to}")
print(f"a != b: {not_equal_to}")
print(f"a > b:{greater_than}")
print(f"a < b:{less_than}")

#define another variable for logical operations
c = 15

# Logical Operations
and_operation = (a > b) and (b > c) #Logical AND
or_operation = (a > b) or (b > c) #Logical OR
not_operation = not (a > b) # Logical NOT

#Print results
print(f"(a > b) and (b > c): {and_operation}")
print(f"(a > b) or (b > c): {or_operation}")
print(f"not(a > b): {not_operation}")
