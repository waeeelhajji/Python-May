# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello Ninjas!'  # Return the string 'Hello World!' as a response


@app.route("/home/<my_name>/ <int:times>")
def home(my_name, times):
    return f"<h2>home  {my_name}</h2>" * times


@app.route("/template/<int:times>")
def index(times):
    return render_template("index.html", x=times)


@app.route("/list")
def lost():
    student_info = [
        {"name": "Ali", "age": 35},
        {"name": "Alaa", "age": 89},
        {"name": "Rim", "age": 96},
        {"name": "khawla", "age": 12},
    ]
    return render_template("list.html", list=student_info)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True, port=5001)    # Run the app in debug mode.
