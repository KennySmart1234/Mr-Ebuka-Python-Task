

letters = "sEmIcOlOn"

count = 0
for character in letters:

    if character != character.upper():
        count = count + 1
    
print(count)
