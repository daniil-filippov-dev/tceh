
def read_file(filename):
    print('reading file with read_file()')
    try:
        f = open(filename)
        content = f.read()
    finally:
        f.close()

    return content


def way_better(filename):
    print('reading file with way_better()')
    with open(filename) as f:
        return f.read()


def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        f.write(content)


if __name__ == '__main__':
    # Reading:
    print(read_file('toread.txt'))
    print(way_better('toread.txt'))

    # Writing:
    write_to_file('new.txt', 'Some\ntext!')  # rewrites
    write_to_file('existing.txt', 'New line\n', mode='a')  # adds
