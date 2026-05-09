

age = int(input("Enter your age "))

if(age < 5):
    print("Free for you")
    
elif(age >= 5 and age <= 12):
    print("price $5") 
    
elif(age >= 13 and age <= 64):
    print("price $12")        

if(age > 65):
    print("price $8")    
