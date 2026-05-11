

letter = input("Type a sentence: ")
space = 0
count = 0
for character in letter:
    if character == " ":
        space = space + 1
    else:    
        count = count + 1

print("Total word count ", count)    






