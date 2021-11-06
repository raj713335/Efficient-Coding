
def min_fairness(lst,k):
    lst = sorted(lst)
    min_x=1000000000000000000000000000000000000000000000000
    
    for i in range(0, len(lst)-k+1):
        if max(lst[i:i+k])- min(lst[i:i+k])<min_x:
            min_x = max(lst[i:i+k])- min(lst[i:i+k])
            
    return min_x
  
  
# def min_fairness(lst,k):
#     lst = sorted(lst)
#     n = len(lst)
#     return min([abs(lst[i+k-1]-lst[i]) for i in range(n-k+1)])

k=int("2")
l=list(map(int,"8,14,20,10,15".split(",")))
print(min_fairness(l,k))
