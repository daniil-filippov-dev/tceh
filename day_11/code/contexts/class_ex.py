class File(object):
    def __init__(self, filename, mode):
        print('__init__')
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('opening file')
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print('closing file')
        self.open_file.close()


with File('to_open.txt', 'w') as f:
    f.write('some data')

# Note how error is handled:
with File('does-not-exist', 'r') as new_file:
    print(new_file.read())
