import re

def match_pattern(s):
    return bool(re.fullmatch(r"a*b*", s))

print(match_pattern("a"))
print(match_pattern("ab"))
print(match_pattern("abb"))
print(match_pattern("b"))
print(match_pattern("ac"))  # False
