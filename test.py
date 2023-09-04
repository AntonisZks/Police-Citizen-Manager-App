# Dictionary with values that depend on other values in the dictionary
my_dict = {
    'a': 5,
    'b': 10,
    'c': lambda x: x['a'] + x['b'],  # Value of 'c' is calculated based on 'a' and 'b'
}

# Accessing the calculated value
result = my_dict['c'](my_dict)

print(result)  # Output will be 15 (5 + 10)
