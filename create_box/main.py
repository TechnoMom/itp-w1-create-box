"""This is the entry point of the program."""

def create_box(height, width, character):
	box = ''
	line = width * character + '\n'
	counter = 0
	while counter < height:
		box += line
		counter += 1
	return box
    
if __name__ == '__main__':
    box = create_box(3, 4, '*')
    print(box)


# :D :D :D haha!