from flask import Flask, request, send_file
import time

from image_editor import toggle
from image_maker import make_image

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def result():
	if request.method == "GET":
		make_image()
	if request.method == "POST":
		xPos = int(request.form["x"])
		yPos = int(request.form["y"])
		toggle(xPos, yPos)
		make_image()
	return send_file("static/image.png", mimetype="image/png")

if __name__ == '__main__':
	app.run(port=5000, host="0.0.0.0")
