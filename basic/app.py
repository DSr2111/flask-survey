from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

RESPONSES_KEY = "responses"
app = Flask(__name__)

app.config['SECRET_KEY'] = "never-tell"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

@app.route("/")
def show_survey_start():
    """Pick survey to begin."""
    return render_template("survey_start.html", survey=survey)



@app.route("/begin", methods=["POST"])
def start_survey():
    """Begin survey."""
    session[RESPONSES_KEY] = []

    return redirect("/questions/0")


@app.route("/answer", methods=["POST"])
def handle_question():
    """Save responses and continue to next question."""
    choice = request.form['answer']

    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses

    if (len(responses)== len(survey.questions)):
        return redirect("/complete")
    
    
