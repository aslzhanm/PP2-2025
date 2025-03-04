import re

def match_pattern(s):
    return bool(re.fullmatch(r"a.*b", s))

print(match_pattern("axb"))      # True
print(match_pattern("a123b"))    # True
print(match_pattern("ab"))       # True
print(match_pattern("abc"))      # False
print(match_pattern("bxa"))      # False
