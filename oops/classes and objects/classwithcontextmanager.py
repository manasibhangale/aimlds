### Assignment 14: Class with Context Manager

#Create a class named `FileManager` that implements the context manager protocol to open and close a file. Use this class to read the contents of a file.

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Test
with FileManager('sample.txt', 'r') as file:
    content = file.read()
    print(content)