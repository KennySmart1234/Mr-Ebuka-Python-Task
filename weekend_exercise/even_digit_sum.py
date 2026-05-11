


number = int(input("Enter a number "))

sum = 0

while(0 < number):

    extracted = number % 10
    number = number // 10
    
    if extracted % 2 == 0:
        sum = sum + extracted
        
print("even digit sum: ", sum)


