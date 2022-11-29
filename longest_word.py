a=input("Enter the string ")
words=str.split(a)
word=""
l=0
for x in words:
    if (len(x)>l):
        word=x
        l=len(x)
print ("The longest word is ",word,"and the length is ",l)