from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "never-tell"

debug = DebugToolbarExtension(app)

@app.route("/")
def show_survey_start():
    """Pick survey to begin."""




@app.route("/")
def start_survey():
    """Begin survey."""


@app.route("/")
def handle_question():
    """Save responses and continue to next question."""
