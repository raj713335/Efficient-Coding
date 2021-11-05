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
