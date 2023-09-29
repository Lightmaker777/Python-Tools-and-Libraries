# string_mod.py

def concatenate_strings(str1, str2):
    return str1 + str2

def create_string_from_list(string_list):
    return ''.join(string_list)

def has_digit(input_string):
    return any(char.isdigit() for char in input_string)
