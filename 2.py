#swap two elements in a list

#l=[11,2,3,5,8]
l=[23, 65, 19, 90]
pos1=1
pos2=3
op=l[pos1],l[pos2]=l[pos2],l[pos1]
print(l)

def swapPositions(list, pos1, pos2): 
    list[pos1],list[pos2] = list[pos2],list[pos1] 
    return list
  
# Driver Code 
List = [23, 65, 19, 90] 
pos1, pos2  = 1, 3
print(swapPositions(List, pos1-1, pos2-1)) 