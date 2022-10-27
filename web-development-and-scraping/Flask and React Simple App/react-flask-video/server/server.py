#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


# members API route
@app.route('/members')
def members():
    return {'members': ['Member 1', 'Member 2', 'Member 3', 'Member 4', 'Member 5']}


if __name__ == '__main__':
    app.run(debug=True)
