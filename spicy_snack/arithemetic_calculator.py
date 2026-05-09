

numberOne = int(input("Enter a number: "))
numberTwo = int(input("Enter another number: "))
arithmetic_operator  = (input("Enter arithemetic operator to use(+,-,*,/): "))


if arithmetic_operator == "+":
    print(numberOne + numberTwo)
    
if arithmetic_operator == "-":
    print(numberOne - numberTwo) 
       
if arithmetic_operator == "*":
    print(numberOne * numberTwo)

if arithmetic_operator == "/":
    print(numberOne // numberTwo)
