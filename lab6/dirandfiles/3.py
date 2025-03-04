import os

def check_path(path):
    if os.path.exists(path):
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist.")

check_path("example.txt")
