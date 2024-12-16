from flask import Flask
app = Flask(__name__)

@app.route('/')
def redirect_to_link():
    # return redirect method, NOTE: replace google.com with the link u want
    return redirect('https://tringcoin.com/')
if __name__ == '__main__':
    app.run()
