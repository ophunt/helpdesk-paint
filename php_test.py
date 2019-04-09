import subprocess

image_string = "011"*33+"0"

subprocess.call(["php", "image_maker.php", "-q", image_string])
