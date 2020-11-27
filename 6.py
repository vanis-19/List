#program to find smallest number in a list
l=[10,67,86,90,9]
l.sort(reverse=True)
print(l[-1])
min1=l[0]
for i in range(len(l)):
    if l[i]<min1:
        min1=l[i]
print(min1)   

print(max(l))