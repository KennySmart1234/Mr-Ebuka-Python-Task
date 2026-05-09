
            
letter = input("Enter a letter: ")

if len(letter) == 1 and letter.isalpha():

    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")

    else:
        print("Consonant")

else:
    print("Invalid input")            
         
