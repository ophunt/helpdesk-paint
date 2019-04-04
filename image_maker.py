from PIL import Image, ImageDraw
import numpy as np
from image_save_load import load_image

def make_image():
	image_array = load_image("image.data")

	squares = len(image_array)
	scale = 10
	size = squares * scale

	img = Image.new("1", (size, size))

	pixels = img.load()

	for i in range(squares):
		for j in range(squares):
			for s in range(scale):
				for t in range(scale):
					pixels[10*i+s,10*j+t] = int(image_array[i][j])

	img.save("static/image.png")

if __name__ == "__main__":
	make_image()
