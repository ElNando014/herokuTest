from flask import Flask, render_template, Response
import cv2


app = Flask(__name__)

@app.route('/')
def index():
    return ("Hello")

if __name__ == '__main__':
    app.run(debug=True)