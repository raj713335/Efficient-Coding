def get_special_count(s):
    count = len(s)
    
    for x in range(0,len(s)):
        y = x
        while y< len(s)-1:
            y+=1
            if s[x] == s[y]:
                count += 1
            else:
                if s[x:y] == s[y+1:2*y-x+1]:
                    count += 1 
                break
    return count
        

s = "mnonopoO"
print(get_special_count(s))


"""
def get_special_count(s):
    n=len(s)
    l=[]
    count =0
    cur=None

    #group the continuously occurring sub-strings with their respective count
    for i in range(n):
        if(s[i] == cur):
            count+=1
        else:
            if(cur is not None):
                l.append((cur,count))
            cur=s[i]
            count = 1
    l.append((cur, count))
    ans=0
    #count the number of substrings that can be formed with a continuously occurring substring
    for i in l:
        ans+=(i[1]*(i[1] + 1))//2
    #count the substrings that can be formed such that all elements are same except the middle one
    for i in range(1, len(l) -1):
        if(l[i-1][0]==l[i+1][0] and l[i][1]==1):
            ans+=min(l[i-1][1], l[i+1][1])
    
    return (ans)

s = "mnonopoO"
print(get_special_count(s))
"""
