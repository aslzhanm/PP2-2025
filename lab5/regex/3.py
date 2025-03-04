import re

def find_sequences(s):
    return re.findall(r"\b[a-z]+_[a-z]+\b", s)

print(find_sequences("abc_def ghi_jkl mno pq_rs"))
