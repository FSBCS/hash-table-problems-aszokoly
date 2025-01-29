def k_most_frequent(lst, k):
    values = {}

    for i in lst:
        if i not in values:
            values[i] = 1
        else:
            values[i] += 1
    
    #lambda part is essentialy def key(x): return values[x]    
    leaderboard = sorted(values.values(), key=lambda x:values[x], reverse=True)
    leaderboard[k]

lst = [1,2,1,1,2]
print(k_most_frequent(lst, 2))



        
