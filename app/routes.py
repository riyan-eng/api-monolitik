from app import app, responses
from app.controllers import test

@app.route('/')
def index():
    return test.cekcek()