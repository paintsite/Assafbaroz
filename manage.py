import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
   app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
