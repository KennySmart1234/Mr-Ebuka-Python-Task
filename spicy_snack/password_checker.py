

password = input("Enter your password: ")


password = len(password)


if(password > 10):
    print("Strong password")
    
elif(password > 6 and password <= 10):
    print("Medium password")    
    
elif(password >= 1 and password <= 6):
    print("Weak password")
    
elif(password < 1):
    print("invalid password")        







