a=[int(x) for x in (input("Enter list of numbers").split())]
a=[int(x*x) for x in a if x in range(32,100) ]
p=[]
num=[]
for x in a:
    num=str(x)
    for y in num:
        if int(y)%2==1:
            break
    else:
        p.append(x)
if len(p)!=0:
    print (p)
else:
    print("no numbers entered has a perfect square with all digits even number")