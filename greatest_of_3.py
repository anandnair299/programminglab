#14. Find biggest of 3 numbers entered 
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>=b and a>c :
        print(a,"is the biggest")
elif b>=a and b>=c :
        print(b,"is the biggest")
else :
        print(c,"is the biggest")