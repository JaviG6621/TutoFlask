from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def my_microservice():
    print(request)
    print(request.environ)
    response = jsonify({'Hello': 'World'})
    print(response)
    print(response.get_data(as_text=True))
    return response



if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)