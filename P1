import math
def sum_dig(n):
    s=0
    while n!=0:
        s+=n%10
        n=n//10
    return s
def prod_dig(n):
    p=1
    while n!=0:
        p*=n%10
        n=n//10
    return p
def Special(n):
    if sum_dig(n)+prod_dig(n)==n:
        return True
    else:
        return False
nod=int(input("Enter a number of digits of the number: "))
for i in range(int(math.pow(10,nod-1)),int(math.pow(10,nod))):
    if Special(i):
        print(i)


