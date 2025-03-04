import re

def camel_to_snake(s):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()

print(camel_to_snake("HelloWorldExample"))  # hello_world_example
