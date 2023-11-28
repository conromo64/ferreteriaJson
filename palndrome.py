import re

# Code challenge es palindorme
# "eye" - true
# "area" - false
# "Anita, la gorda lagartona, no traga la droga latina" -
# "Sé Verlas aL Reves"

def is_palindrome(input_string):
    ##input_string = input_string.replace(" ", "").lower()
    input_string = re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()
    print(input_string)
    print(input_string[::-1])

    return input_string == input_string[::-1]

print(is_palindrome("asi mario oira misa"))