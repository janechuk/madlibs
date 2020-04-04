from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)



@app.route('/')
def home_page():
    """Return homepage."""
    prompts = story.prompts
    return render_template("index.html", prompts=prompts)

@app.route('/story')
def story_page():
    """Return homepage."""
    text = story.generate(request.args)
    return render_template("story.html", text=text)