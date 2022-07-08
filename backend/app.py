from flask import Flask

app = Flask(__name__)

class kk :
    def __init__(self, first, second):
        self.first = first
        self.second = second

@app.route('/')
def hello_world():
    a = kk(2,4)# put application's code here
    return a


if __name__ == '__main__':
    app.run()
