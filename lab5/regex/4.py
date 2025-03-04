import re

def find_sequences(s):
    return re.findall(r"[A-Z][a-z]+", s)

print(find_sequences("Hello World Python Code"))
