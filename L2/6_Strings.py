# ord(), find smth
character = 'A'
unicode_char = ord(character)  # Similar to ASCII
print(unicode_char)

# 1. Indexing

s = "Norwegian Wood"
print(s[1])  # 'o'

# 2. Length
print(len(s))

# 3. 'in' keyword
existence = "Wood" in s  # Case sensitive
print(existence)

# 4. Formatted Strings

# there are many ways to format strings, we'll look over the most popular method

a = input("Enter name: ")
b = input("Enter opponent's name: ")
print('My name is', a)  # String formatting
print(f'My name is {a}, and my opponents name is ')  # String interpolation


# https://www.w3schools.com/python/python_strings_methods.asp
