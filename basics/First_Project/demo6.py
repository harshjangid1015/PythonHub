#The WHILE Loop
var=1
while (var<=10):
    print("Hi! I am", var)
    var=var+1
print("")
print("Good Bye!")

#The FOR Loop
count=0
print("Enter your name :")
name=input()
for letter in name:
    if (letter in['A','E','I','O','U','a','e','i','o','u']):
        count=count+1
print("You have", count, " in your name.")

