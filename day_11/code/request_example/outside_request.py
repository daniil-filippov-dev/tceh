from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'hello world!', 200

# print(request, type(request), request.method)

# with app.test_request_context('/?next=http://example.com/'):
#     print(request, type(request), request.method)

if __name__ == '__main__':
    app.run()
