d1={'a':'1'}
d2={'a':'2'}
d3={**d1,**d2}
for k,v in d3.items():
    if k in d1 and k in d2:
        d3[k]=[v,d1[k]]
print(d3)
