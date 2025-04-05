def group_anagrams(strs):
    from collections import defaultdict
    
    anagram_groups = defaultdict(list)
    
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagram_groups[sorted_s].append(s)
    
    return list(anagram_groups.values())

size = int(input("Enter Size: "))
arr = []
for i in range(size):
    strin = input()
    arr.append(strin)
print(group_anagrams(arr))