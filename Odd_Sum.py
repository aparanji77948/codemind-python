n=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
   if(i%2!=0):
       s=s+i
print(s)