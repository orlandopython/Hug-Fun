import hug
from random import randint

@hug.get(examples='number=30')
@hug.local()
@hug.cli()
def fizzbuzz(number: hug.types.number):
    s = ''
    if not number % 3:
        s += 'Fizz'
    if not number % 5:
        s += 'Buzz'
    return s or number

@hug.get()
@hug.cli()
def randomList(number: hug.types.number,maxNum: hug.types.number=5):
    return [randint(0,maxNum) for _ in range(number)]

strings = []

@hug.put('/string')
def put_str(string: hug.types.text):
    """Add a string to string list"""
    global strings
    strings.append(string)
    return strings

@hug.get('/string')
def get_str():
    """Get string list"""
    return strings

@hug.delete('/string')
def rem_str(string: hug.types.text):
    global strings
    strings.remove(string)
    return strings

if __name__ == '__main__':
    randomList.interface.cli()

