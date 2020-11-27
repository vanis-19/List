#find second largest number in a list
l=[1,6,9,3,6]
max1=l[0]
smax=max1
for i in range(len(l)):
    if l[i]>max1:
        max1=l[i]
        smax=max1
print(smax)  

l.sort()
print(l[-2])

