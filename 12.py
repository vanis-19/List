#Remove empty List from List

test = [5, 6, [], 3, [], [], 9]
res = [i for i in test if i!=[]]
print(res)