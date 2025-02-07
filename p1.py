
def group_anagrams(words):
    groups= {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = [word]
        else:
            groups[key].append(word)

    return list(groups.values())

    
        
words = ['tea', 'eat', 'tan', 'nat','bat']
group_anagrams(words)
    
