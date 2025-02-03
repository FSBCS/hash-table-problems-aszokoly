def k_most_frequent(lst, k):
    values = {}

    for i in lst:
        if i not in values:
            values[i] = 1
        else:
            values[i] += 1
    
    #lambda part is essentialy def key(x): return values[x]    
    leaderboard = sorted(values.keys(), key=lambda x: values[x], reverse=True)
    leaderboard[k - 1]
    
    while k > 1:
        k -= 1
        leaderboard[k]
    
    print(leaderboard)

lst = [1,2,1,3,1,2]
k_most_frequent(lst, 2)





        
