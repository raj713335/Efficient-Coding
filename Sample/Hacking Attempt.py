#inputx = ["4", "2", "R", "Y", "G", "Y"]
inputx = list(map(str, input().split(" ")))
N, K = int(inputx[0]), int(inputx[1])
Lights = inputx[2:]

traffic_lights = {"G": 0, "R": 1, "Y": 2}
arrayx = []

for each in Lights:
    arrayx.append(traffic_lights[each])

iterx = 0
count = 0
while sum(arrayx) != 0 and iterx < N:
    rangex = min(N, iterx+1+K-1)
    if arrayx[iterx] == 0 or arrayx[iterx] % 3 == 0:
        iterx += 1
        continue
    else:
        for i in range(iterx, rangex):
            arrayx[i] += 1
        count += 1

print(count)


"""
def getCount(N,K,given_state):
    total = 0
    current = 0
    temp_state = [0]*N
    for i in range(N):
        if(i>=K):
            current = (current - temp_state[i-K])%3
        t = (given_state[i] + current) % 3
        processNumber = (3-t)%3
        total +=processNumber
        current = (current+processNumber)%3
        temp_state[i] = processNumber
    return total

N,K = (int(x) for x in "4 2".split())
m={'G':0,'R':1,'Y':2}
given_state=[m[x] for x in "R Y G Y".split()]

print(getCount(N,K,given_state))

"""






"""
4 2 R Y G Y -> 5
"""
