s=input("Enter a string: ")
lv=['a','e','i','o','u']
ls=[]
for i in s:
    if i in lv:
        ls.append(s.index(i))
if len(ls)>2:
    d=ls[1]-ls[0]
j=True
for j in range(2,len(ls)):
    if (ls[j]-ls[j-1])!=d:
        j=False
        break
if j:
    print("It is a nice string!")
else:
    print("It is not a nice string!")