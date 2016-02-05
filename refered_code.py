"""
Thai Code refered source code
"""

# Numberical Declaration & Manipulation
var_integer = 2
var_float = 3.14
var_boolean = True
var_complex = 2 + 0.5j
var_expr = var_integer * 5 + var_float

# Numberical Function
var_rounded = round(var_expr, 2)

# String Declaration & Manipulation
var_string = "Hello!"
var_string_d = var_string[2:]
var_string_c = var_string + var_string_d

# String Function
print(var_string)
print(var_string_d)

var_string_l = len(var_string_c)

# List Declaration & Manipulation
squares = [1, 4, 9, 16, 25]
new_sqr = squares + [36, 49, 64, 81, 100]
cubes = [1, 8, 27, 65, 125]
cubes[3] = 4 ** 3

# List Function
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

# Nested List
list_a = ['a', 'b', 'c']
list_n = [1, 2, 3]
list_x = [a, n]
print(list_x)
print(list_x[0])
print(list_x[0][1])

# If Statement
if boolean_expr:
    statements
elif boolean_expr:
    statements
else:
    statements

# While Statements
fib_a, fib_b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

# For Statements
for var_iter in var_array:
    statements
