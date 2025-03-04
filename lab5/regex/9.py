import re

def insert_spaces(s):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", s)

print(insert_spaces("HelloWorldExample"))  # Hello World Example
