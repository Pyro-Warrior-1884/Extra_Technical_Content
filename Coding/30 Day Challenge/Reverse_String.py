def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result


input_string = input()
print(reverse_words(input_string))

