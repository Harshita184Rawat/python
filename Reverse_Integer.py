x = 123       
number=str(x)
n=len(number)
reversed=[]
for i in range(n):
    reversed.append(int(number[n-1]))
    n=n-1
print(reversed)
y=len(number)
final=0
for num in reversed:
    final=final+num*(pow(10,(y-1)))
    y=y-1
    
print(final)