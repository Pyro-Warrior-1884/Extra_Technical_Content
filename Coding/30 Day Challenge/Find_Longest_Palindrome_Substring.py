def longest_palindrome(s):
    if len(s) <= 1:
        return s

    LPS = ""

    for i in range(1, len(s)):

        # Consider odd length palindromes
        low = i
        high = i
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1

        palindrome = s[low + 1:high]
        if len(palindrome) > len(LPS):
            LPS = palindrome

        # Consider even length palindromes
        low = i - 1
        high = i
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1

        palindrome = s[low + 1:high]
        if len(palindrome) > len(LPS):
            LPS = palindrome

    return LPS

s = input()
print(longest_palindrome(s))