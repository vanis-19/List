#Remove multiple elements from a list in Python
l = [11, 5, 17, 18, 23, 50]  
for i in l:
    if i%2==0:
        l.remove(i)
print(l)       
