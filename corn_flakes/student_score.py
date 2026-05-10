


count = 0
for scores in range(1, 16):

    score = int(input("Enter the student score: "))
    if score >= 45:
        count = count + 1
    
print("Student that pass: ", count)
print("Student that fail: ", 15 - count)        












