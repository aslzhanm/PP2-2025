import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted.")
    else:
        print("File not found or no permission.")

delete_file("file_to_delete.txt")
