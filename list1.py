a=input("enter first list").split()
a=list(map(int,a))
b=input("enter second list").split()
b=list(map(int,b))
if len(a)==len(b):
    print("the lists a and b are of same length")
else:
    print("a and b are not of same length")
if sum(a)==sum(b):
    print("sum of list a = sum of list b")
else:
    print("sum of lists a and b are not equal")
l = []
for x in a:
    if x in b:
        l.append(x)
if len(l)==0:
    print("no common elements")
else:
    print(l," are the common elements")