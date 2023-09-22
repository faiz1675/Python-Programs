# 88-WAP to find occurrence of each character in string.
def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Test case
text = "Hello, World!"
result = count_characters(text)
print(result)
