import numpy as np
import subprocess

def load_image(path):
	with open(path, "r") as image_file:
		image_data = list(map(list, image_file.read().split()))
		image_array = np.array(image_data).transpose()
	return image_array

def save_image_data(image_array):
	image_array = image_array.transpose()
	save_string = ''.join(list(map(lambda s: ''.join(s), image_array)))
	subprocess.call(["php", "image_save_data.php", "-q", save_string])
