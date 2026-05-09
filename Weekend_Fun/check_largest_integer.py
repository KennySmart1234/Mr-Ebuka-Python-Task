integer_a = int(input("Enter integer a: "))
integer_b = int(input("Enter integer b: "))
integer_c = int(input("Enter integer c: "))


largest_integer = integer_a
if(integer_b > largest_integer):
    largest_integer = integer_b
    
if(integer_c > largest_integer):
    largest_integer = integer_c
    
print("largest integer between a,b,c = ", largest_integer)        
        
  
