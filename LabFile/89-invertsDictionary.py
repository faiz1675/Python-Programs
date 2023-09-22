# 89-WAP that inverts a dictionary. That is, it makes key of one dictionary value of another 
# and vice versa. 
def invert_dictionary(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        inverted_dict[value] = key
    return inverted_dict

# Test case
my_dict = {'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}
inverted_dict = invert_dictionary(my_dict)
print(inverted_dict)
