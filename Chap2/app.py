from flask import Flask


app=Flask(__name__)

@app.route("/")# for example www.google.com/ it represent the '/'
def Home():
    return "hello flask"

@app.route("/sub")
def Sub():
    return "This sub endpoint"
app.run(port=5000)