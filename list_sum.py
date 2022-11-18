def sum(a):
    sum=0
    for i in a:
        sum+=i
    print("Sum = ",sum)

a=[int(x)for x in (input("Enter list elements\n").split())]
sum(a)