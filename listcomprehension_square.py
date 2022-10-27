a=[]
a=input("Enter numbers").split()
a=list(map(int,a))
b=[x*x for x in a if x>0]
print (b)
 
