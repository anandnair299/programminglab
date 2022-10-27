a=input("enter string")
a=list(a)
c=['a','A','e','E','i','I','o','O','u','U']
b=[x for x in a for y in c  if x==y]
print (b)
 
