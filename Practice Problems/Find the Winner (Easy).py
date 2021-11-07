maria = []
andrea = []


maria_score = 0
andrea_score = 0

for i in range(int(input())):
    andrea.append(int(input()))

for i in range(int(input())):
    maria.append(int(input()))

string = str(input())

for i in range(0, min(len(maria), len(andrea))):
    if string == "Even" and i % 2 == 0:

        maria_score += (maria[i] - andrea[i])
        andrea_score += (andrea[i] - maria[i])
        print(i, maria_score, andrea_score)
    elif string == "Odd" and i % 2 != 0:
        maria_score += (maria[i] - andrea[i])
        andrea_score += (andrea[i] - maria[i])
        print(i, maria_score, andrea_score)


print(maria_score, andrea_score)

if maria_score > andrea_score:
    print("Maria")
else:
    print("Andrea")


"""
3
1
2
3
3
2
1
3
Odd
"""


"""
3
1
2
3
3
2
1
3
Even
"""
