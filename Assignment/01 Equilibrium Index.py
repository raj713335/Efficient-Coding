listx = input()


for i in range(0, len(listx)):
    if sum(listx[:i])==sum(listx[i+1:]):
        print(i)
        exit(0)
print(-1)
