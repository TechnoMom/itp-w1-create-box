"""This is the entry point of the program."""

def create_box(height, width, character):
    line = character*width + '\n'
    box = line*height
    return box
    
if __name__ == '__main__':
    box = create_box(3, 4, '*')
    print(box)
