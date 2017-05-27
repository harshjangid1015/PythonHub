mylist=['one', 'two', 'three', 4, 5.1, (6+2j)]
print(mylist)
print(mylist * 3)
print(mylist[3:5])
newlist=[7, 'eight', 9.0]
print (newlist)
print(mylist + newlist)
newlist[0]='seven'
print(newlist)

mytuple=('a word', 'a number', 10)
print(mytuple)

#Dictionaries
address={}
address["John"]="john@gmail.com"
address["Adam"]="adam@gmail.com"
address["Peter"]="peter@gmail.com"
print(address)
new={'apple':'fruit', 'iPhone':'Phone', 7:'a number'}
print (new)
print (address.keys())
print(address.values())
