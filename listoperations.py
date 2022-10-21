a=[]
b=[]
flag=False
a=input("Enter value").split()
a=list(map(int,a))
b=input("enter values").split()
b=list(map(int,b))
if len(a)==len(b):
    print("length of a equals length of b")
else:
    print("length of a not equals length of b")
if sum(a)==sum(b):
    print("sum of a equals sum of b")
else:
    print("sum of a not equals sum of b")
for x in a:
    for y in b:
        if x==y:
            print("Common element present in a and b")
            flag=True
            quit()
if flag==False:
    print("no common elements in a and b")
    
    
            
            
    
