# script.py

# Import functions from math_mod.py
from math_mod import add, subtract, multiply, divide

# Import functions from string_mod.py
from string_mod import concatenate_strings, create_string_from_list, has_digit

# Example usage of math_mod functions
num1 = 4
num2 = 17

result_add = add(num1, num2)
result_subtract = subtract(33, 19)
result_multiply = multiply(3, 23)
result_divide = divide(44, 3)

print(f"Result of adding {num1} and {num2} is {result_add}")
print(f"Result of subtracting 33 and 19 is {result_subtract}")
print(f"Result of multiplying 3 and 23 is {result_multiply}")
print(f"Result of dividing 44 by 3 is {result_divide}")

# Example usage of string_mod functions
str1 = "Hello"
str2 = "DCI"
string_list = ["Hello", "DCI"]
input_string = "HelloDCI007"

result_concatenate = concatenate_strings(str1, str2)
result_create_string = create_string_from_list(string_list)
result_has_digit = has_digit(input_string)

print(f"Result of concatenation of '{str1}' and '{str2}' is {result_concatenate}")
print(f"Result of creating string from list {string_list} is {result_create_string}")

if result_has_digit:
    print("There is a digit in your string!")
else:
    print("There are no digits in your string.")
