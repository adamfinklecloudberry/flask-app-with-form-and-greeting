from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    greeting = ""
    if request.method == "POST":
        username = request.form["name"]
        greeting = f"Hello, {username}!"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)