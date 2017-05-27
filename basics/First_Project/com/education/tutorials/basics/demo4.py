# IF statement
myvar=50
if myvar<100:
    print("You are short of being 100 percent")
print("Good bye !")

#ELSE statement
myvar=150
if myvar<100:
    print("You are short of being 100 percent")
else:
    print("you are at your best")
print("Good bye !")

#ELIF statement
sp=1500
cp=1200
if (sp>cp):
    print("Congratulations")
    print("You've made a profit of", sp-cp, "bucks")
elif (cp>sp):
    print("Ooops")
    print("You've made a loss of", cp-sp, "bucks")
else:
    print("You didn't make or lose money")

sp=1200
cp=1500
if (sp>cp):
    print("Congratulations")
    print("You've made a profit of", sp-cp, "bucks")
elif (cp>sp):
    print("Ooops")
    print("You've made a loss of", cp-sp, "bucks")
else:
    print("You didn't make or lose money")

sp=1500
cp=1500
if (sp>cp):
    print("Congratulations")
    print("You've made a profit of", sp-cp, "bucks")
elif (cp>sp):
    print("Ooops")
    print("You've made a loss of", cp-sp, "bucks")
else:
    print("You didn't make or lose money")

#ASCII values
print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))

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
