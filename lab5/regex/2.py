import re

def match_pattern(s):
    return bool(re.fullmatch(r"ab{2,3}", s))

print(match_pattern("abb"))   # True
print(match_pattern("abbb"))  # True
print(match_pattern("abbbb")) # False
print(match_pattern("ab"))    # False
