def longest_child(s1,s2):
    n,m=len(s1),len(s2)
    lcs=[[0]*(m+1) for i in range(n+1)]
    for i,c1 in enumerate(s1):
        for j,c2 in enumerate(s2):
            if c1==c2:
                lcs[i][j]=lcs[i-1][j-1]+1
            else:
                lcs[i][j]=max(lcs[i][j-1],lcs[i-1][j])
    return lcs[n-1][m-1]

input_strings = "ABCD,ABDC".split(',')
string1=input_strings[0]
string2=input_strings[1]
print(longest_child(string1,string2))
