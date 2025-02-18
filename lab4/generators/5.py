def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
print(list(countdown(n)))
