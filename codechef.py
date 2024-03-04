# Add powers of 2
n = int(input("Enter n: "))
k = int(input("Enter k: "))
sum = 0
a = 2
b=0


for i in range(n-1,-1,-1):
    
    if sum != k:
        if (sum+n) <k:
            c=pow(a,i)
            sum += c
            b+=1
        if (sum+n) >k:
            sum-=c
            b-=1
        if(sum+n) ==k:
            sum+=n
            break

if sum==k:
    print(b)
else:
    print("Not possible")

