for i in range(int(input())):
    S = str(input())
    
    output = S[0]
    
    for each in S[1:]:
        #print(each, output[-1])
        if each != output[-1]:
            output += each
    print(output)
    
"""
4
abb
aaab
ababa
aabbaa

ab
ab
ababa
aba


"""
