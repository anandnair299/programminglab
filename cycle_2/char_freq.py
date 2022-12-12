def freq(a):
    b={}
    for x in a:
        if x in b:
            b[x]+=1
        else:
            b[x]=1
    print(b)
a=input("Enter string")
freq(a)