def write_list_to_file(filename, data):
    with open(filename, "w") as f:
        f.writelines("\n".join(data))

write_list_to_file("output.txt", ["line1", "line2", "line3"])
