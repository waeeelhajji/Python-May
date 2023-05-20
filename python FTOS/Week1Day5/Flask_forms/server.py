from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "no secrets between us"


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_form():
    print("inside /process")
    print(request.form["ninja_email"])

    session["email"] = request.form["ninja_email"]

#! NEVER EVER EVER RENDER ON A POST - USE REDIRECT

    return redirect("/display")


@app.route("/display")
def disp():
    print(session["email"])

    name = session["email"]

    return render_template("display.html", name=name)


@app.route("/clear")
def clear():
    session.clear()
    print(session)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
