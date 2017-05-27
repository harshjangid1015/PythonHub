#Nested IF-ELSE statement
char=input()
if ord(char)>=65 and ord(char)<=90:
    print("You entered an upper case alphbet.")
    if char in['A', 'E', 'I', 'O', 'U']:
        print("You enetered a vowel.")
    else:
        print("You enetered a consonant.")
elif ord(char)>=97 and ord(char)<=122:
    print("You entered an lower case alphbet.")
    if char in['a', 'e', 'i', 'o', 'u']:
        print("You enetered a vowel.")
    else:
        print("You enetered a consonant.")
else:
    print("You did not enter an alphabet")
