"""This is the entry point of the program."""

def create_box(height, width, character):
    my_box = width*character + '\n'
    return height * my_box

if __name__ == '__main__':
    my_box = create_box(3, 4, '*')
    print(my_box)
