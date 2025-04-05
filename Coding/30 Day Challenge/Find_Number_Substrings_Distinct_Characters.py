s = input()
k = int(input())

strings = []
if k <= len(s):
    string =""
    for i in range(0,len(s),1):
        for j in range(i,len(s),1):
            string = s[i:j+1]
            st = set(string)        
            if len(st) == k:
                strings.append(string)
    print(strings)
    print(len(strings))
else:
    print("Invalid")
    
