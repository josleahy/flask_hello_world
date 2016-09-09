from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
    """
    return html.format(name.title())

@app.route("/jedi/<first>/<last>")
def jedi(first, last):
    return "The force is strong with you, {}".format(last[:3]+first[:2] + "!")

if __name__ == "__main__":
    app.run()
