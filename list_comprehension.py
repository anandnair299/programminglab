#a=[int(x) for x in input("enter first list").split()]
#print(f"positive integers are{[x for x in a if x > 0]}")
#print(f"the squares are{[x*x for x in a]}")

c=['a','A','e','E','i','I','o','O','u','U']
b=[input("Enter a word")]
l=[x for x in b if x in c]
print(l)