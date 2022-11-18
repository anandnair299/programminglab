a=[int(x) for x in (input("Enter numbers ").split())]
a=[int(x*x) for x in a if x in range(32,1000) ]
print (a)