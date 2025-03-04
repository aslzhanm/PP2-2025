def count_case(s):
    return sum(1 for c in s if c.isupper()), sum(1 for c in s if c.islower())

print(count_case("HelloWorld"))
