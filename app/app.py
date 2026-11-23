from flask import Flask, render_template, Response


app = Flask(__name__)


@app.route("/")
def index():
    string = render_template("saludo.html")
    response = Response(string)
    return response


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)