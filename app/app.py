from flask import*


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("saludo.html")

if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)

