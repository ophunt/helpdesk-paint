import numpy as np
import subprocess
from image_save_load import load_image

def make_image():
	image_array = load_image("image.data")
	image_string = ''.join(list(map(lambda s: ''.join(s), image_array)))

	subprocess.call(["./image_maker.php", "-q", image_string])

if __name__ == "__main__":
	make_image()
