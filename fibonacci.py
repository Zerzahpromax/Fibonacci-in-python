a=int(input("Enter a number"))
n1,n2=0,1
print(n1,n2)
for i in range(2,a):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)