s= input()

store = set(s)
string = ""
max_len = 0
count = 0

for i in range(len(s)):
    if s[i] not in string:
        string += s[i]
        count += 1
    else:
        if count > max_len:
            max_len = count
        count = 1
        string = s[i]
        
    if len(string) == len(store):
        max_len = len(string)
        break   

print(max_len)        
