"""This is the entry point of the program."""

def create_box(height, width, char):
	count = 0
	box = ''
	while count < height:
		box += char * width + '\n'
		count += 1
	print(box)
	return box

if __name__ == '__main__':
    box = create_box(3, 4, '*')
    print(box)
