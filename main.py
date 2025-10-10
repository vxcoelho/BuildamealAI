from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message='Build-A-Meal - Coming Soon!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
