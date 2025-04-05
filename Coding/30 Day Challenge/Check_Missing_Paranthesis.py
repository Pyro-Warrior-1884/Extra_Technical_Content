string = input()

if len(string)%2 == 1:
    print("false")

else:
    count = 0
    store = {'[':']', '{':'}', '(':')'}
    str_size = len(string)
    for i in range(str_size//2):
        if store[string[i]] in store:            
            if store[string[i]] == string[len(string)-1-i]:
                count += 1
            else:
                print('false')
                break
        else:
            print('false')
            break
    
    if count == (len(string)//2):
        print('true')
    
            
    
    