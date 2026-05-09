

total_bill = int(input("Enter total bill: "))
is_member = input("is member(yes or no): " )



if total_bill >= 1000 and is_member == "yes":

    print("10% off")
    
elif total_bill >= 1000 and is_member != "yes":

    print("5% off")
    
else:
    print("No discount")        
    
    
