import math
def Kaprekar(n):
    s=n**2
    nod=int(math.log10(n))+1
    k=s%(10**nod)+s//(10**nod)
    if k==n:
        return True
    else:
        return False
num=int(input("Enter a number: "))
if Kaprekar(num):
    print(num," is a Kaprekar Number!")
else:
    print(num, " is not a Kaprekar Number!")
