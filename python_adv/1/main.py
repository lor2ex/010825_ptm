from flask import Flask

app = Flask(__name__)
@app.route("/") # Задание 1, не хватало /
def home():
    return "Hello, Flask!"

@app.route("/user/<name>") # Задание 2
def greetings(name):
    return f"Greetings, {name}"


if __name__ == "__main__":
    app.run(debug=True)