import numpy as np

def load_image(path):
	with open(path, "r") as image_file:
		image_data = list(map(list, image_file.read().split()))
		image_array = np.array(image_data).transpose()
	return image_array

def save_image(path, image_array):
	image_array = image_array.transpose()

	save_string = ""
	for row in image_array:
		save_string += "".join(row) + "\n"

	with open("image.data", "w") as image_file:
		image_file.write(save_string)
