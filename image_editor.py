import numpy as np
from image_save_load import save_image, load_image
from image_maker import make_image

def clear():
	image_array = np.full((10,10), "0")
	save_image("image.data", image_array)

def toggle(x, y):
	image_array = load_image("image.data")
	image_array[x][y] = str(1 - int(image_array[x][y]))
	save_image("image.data", image_array)

def main():
	clear()
	toggle(0,0)
	for i in range(10):
		toggle(i,9-i)

	make_image()

if __name__ == "__main__":
	main()
