# Build a context manager for safe file handling
class SafeFileHandler:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
with SafeFileHandler('/Users/hchethankumar/Desktop/python_workspace/Day17/example.txt', 'w') as f:
    f.write('Hello, World!')

with SafeFileHandler('/Users/hchethankumar/Desktop/python_workspace/Day17/example.txt', 'r') as f:
    content = f.read()
    print(content)