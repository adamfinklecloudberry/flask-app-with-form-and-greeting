from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """Prompts the user to enter a name and displays it"""
    greeting = ""
    if request.method == "POST":
        username = request.form["name"]
        greeting = f"Hello, {username}!"
    return render_template("index.html", greeting=greeting)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    """Prompts the user to enter feedback and displays it"""
    response = ""
    if request.method == "POST":
        feedback = request.form["feedback"]
        response = f"Thank you for your feedback: '{feedback}'"
    return render_template("feedback.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)