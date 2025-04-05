def generate_permutations(s):
    def permute(chars, left, right, result_set):
        if left == right:
            result_set.add(''.join(chars))  
        else:
            for i in range(left, right + 1):
                chars[left], chars[i] = chars[i], chars[left]  
                permute(chars, left + 1, right, result_set) 
                chars[left], chars[i] = chars[i], chars[left]  
    
    result_set = set()  
    permute(list(s), 0, len(s) - 1, result_set)      
    return list(result_set)  

string = input()
print(generate_permutations(string))  
