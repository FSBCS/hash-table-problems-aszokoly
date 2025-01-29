
def group_anagrams(words):
    anagrams = {}
    for i in words:
        values = ''.join(sorted(i))
    
        if values not in anagrams:
            anagrams[values] = []

        anagrams[values].append(i)
    return list(anagrams.values())
        
words = ['tea', 'eat', 'tan', 'nat','bat']
print(group_anagrams(words))
    
