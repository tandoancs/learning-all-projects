from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def greeting():
    return {'message': 'Hello, This is first web service using Python and Flask framework!'}


if __name__ == "__main__":
    app.run(debug=True)
