#Data Type conversion
print(int (55.89))

print(float (36))

my_strint=str(9500)
print(my_strint)
print (my_strint [1])

print (tuple ("This is a string"))

print(list ("This will be a list"))

print(chr (65))

print(ord ('a'))

print(hex (4500))

print(oct (4500))

print(bin (42))

#Airthmatic Operation
print(10+15)
print(15-10)
print(15*10)
print(15/10)
print(15%10)
print(3**2)
a=15
b=10
print (a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Bitwise & Logical Operator
a=15
b=10
print (bin (a))
print(bin (b))
print(bin (a&b))
print(bin (a or b))
print(bin (a^b))

a=True
b=False
print (a and b)
print(a or b)
print(not a)
print(not b)

#Membership & Identity operator
str1="I have a lazy dog"
print (str1)
print ('dog' in str1)
print('lion' in str1)
mylist=[1, 3, 19, 32, 48, 77]
print(65 in mylist)
print(19 in mylist)

a=42
b='42'
print (a is b)
c=42
print(a is c)
print(a is not b)

print(5+4*2)
print((5+4)*2)
