import re

def split_uppercase(s):
    return re.split(r"(?=[A-Z])", s)

print(split_uppercase("HelloWorldExample"))  # ['Hello', 'World', 'Example']
