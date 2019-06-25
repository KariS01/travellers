from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html", title='Contact')


@app.route("/process", methods=["POST"])
def process():
    name = request.form['name']
    email = request.form['email']
    return render_template("contact.html", title='Contact', name=name.title())

@app.route("/hotels")
def hotels():
    return render_template("hotels.html", title='Hotels')

app.run(debug=True)