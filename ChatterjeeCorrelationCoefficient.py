import random
import math
def list_input(n):
    l=[]
    for i in range(n):
        l.append(int(input("Enter element: ")))
    return l
def Rank_F(ls):
    f_rank=[]
    for i in ls:
        f=0
        for j in ls:
            if i[1]>=j[1]:
                f=f+1
        f_rank.append(f)
    return f_rank
def Rank_R(ls):
    r_rank = []
    for i in ls:
        r=0
        for j in ls:
            if i[1] <= j[1]:
                r=r+1
        r_rank.append(r)
    return r_rank
n=int(input("Enter number of elements: "))
print("Enter elements of first list: ")
X=[]
Y=[]
X=list_input(n)
print("Enter elements of second list: ")
Y=list_input(n)
Uniq=[]
Uniq.append(X[0])
for i in X:
    if i in Uniq:
        continue
    else:
        Uniq.append(i)
T=[]
for i in range(n):
    T.append((X[i],Y[i]))
T.sort()
d={}
for i in Uniq:
    d[i]=[]
    for j in T:
        if j[0]==i:
            d[i].append(j)
for i in d.keys():
    random.shuffle(d[i])
R=[]
for j in d.values():
    R+=j
print("Rearranged pairs of random variables (X,Y): ",R)
sum_num=0
fr=Rank_F(R)
rr=Rank_R(R)
for i in range(len(fr)-1):
    sum_num+=int(math.fabs(fr[i+1]-fr[i]))
CCC=0.0
if len(Uniq)==n:
    CCC=1-((3*sum_num)/((n**2)-1))
else:
    s=0
    for i in range(len(rr)):
        s+=rr[i]*(n-rr[i])
    CCC=1-((n*sum_num)/(2*s))
print("Chatterjee Correlation Coefficient: ",CCC)