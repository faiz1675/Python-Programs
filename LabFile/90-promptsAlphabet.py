# 90-WAP that prompts user to enter an alphabet and then print all the words that starts with 
# that alphabet from the list of words.

def print_words_starting_with(alphabet, words):
    for word in words:
        if word.startswith(alphabet):
            print(word)

# Test case
word_list = ["apple", "banana", "cat", "dog", "elephant", "fish"]
user_input = input("Enter an alphabet: ")
print("Words starting with", user_input + ":")
print_words_starting_with(user_input, word_list)