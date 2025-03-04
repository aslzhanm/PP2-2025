def count_lines(filename):
    with open(filename, "r") as f:
        print("Number of lines:", sum(1 for line in f))

count_lines("example.txt")
