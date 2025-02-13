from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


feedback_list = []


@app.route("/", methods=["GET", "POST"])
def home():
    greeting = ""
    if request.method == "POST":
        username = request.form["name"]
        greeting = f"Hello, {username}!"
    return render_template("index.html", greeting=greeting)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        try:
            feedback = request.form["feedback"]
            feedback_list.append(feedback)  # Store feedback in the list
            return redirect(url_for('feedback'))  # Redirect to the same page to avoid resubmission
        except KeyError:
            return "Error: Feedback field is missing.", 400
        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    return render_template("feedback.html", feedback_list=feedback_list)


@app.route("/delete_feedback/<int:index>", methods=["POST"])
def delete_feedback(index: int):
    if 0 <= index < len(feedback_list):
        feedback_list.pop(index)
    return redirect(url_for("feedback"))


if __name__ == "__main__":
    app.run(debug=True)
