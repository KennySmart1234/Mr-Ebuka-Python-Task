

father_age = int(input("Enter current father's age: "))
son_age = int(input("Enter current son age: "))



if (son_age >= 1 and father_age <= 80):

    if(son_age < father_age):
        twice_old = (father_age - (son_age * 2))
        
        if twice_old >= 0:
            print("Father twice son age ", twice_old, "year(s) ago")
        if twice_old < 0:
            print("Father will twice son age", (twice_old * -1), "in coming year(s)")
        
          
else:
    print("Age out of range")
       



















