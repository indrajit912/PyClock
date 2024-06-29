# A flask app to preview the current time
# Author: Indrajit Ghosh
# Created on: Jun 30, 2024
# 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000)
