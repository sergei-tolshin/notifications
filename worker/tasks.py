import time

from main import app


@app.task
def check():
    time.sleep(10)
    print('I amchecking your stuff')


@app.task
def test(name=None):
    time.sleep(10)
    print(f'Hello, {name}')
