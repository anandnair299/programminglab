def fact(a):
    fact=1
    while(a>1):
        fact*=a
        a-=1
    print("factorial=",fact)

a=int(input("enter a number"))
fact(a)
