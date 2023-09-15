import flask as Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from a Flask App!"

if __name__ == "__main__":
    app.run(port=8080)