from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    url_for,
    jsonify
)


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
            feedback_list.append(feedback)
            return redirect(url_for('feedback'))
        except KeyError:
            return "Error: Feedback field is missing.", 400
        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    return render_template("feedback.html", feedback_list=feedback_list)


@app.route("/edit_feedback/<int:index>", methods=["GET", "POST"])
def edit_feedback(index):
    if request.method == "POST":
        new_feedback = request.form["feedback"]
        if 0 <= index < len(feedback_list):
            feedback_list[index] = new_feedback
        return redirect(url_for('feedback'))

    # Render the edit form with the current feedback
    current_feedback = feedback_list[index] if 0 <= index < len(feedback_list) else ""
    return render_template("edit_feedback.html", current_feedback=current_feedback, index=index)


@app.route("/delete_feedback/<int:index>", methods=["POST"])
def delete_feedback(index: int):
    if 0 <= index < len(feedback_list):
        feedback_list.pop(index)
    return redirect(url_for("feedback"))


@app.route("/api/feedback")
def get_feedback():
    return jsonify({"feedback_list": feedback_list})


if __name__ == "__main__":
    app.run(debug=True)
