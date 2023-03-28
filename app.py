from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)

app.config['SECRET_KEY'] = "Chickenzforlife"

debug = DebugToolbarExtension(app)

@app.route('/')
def get_keywords():

  prompts = story.prompts

  return render_template('base.html', prompts=prompts)

@app.route('/story')
def render_story():
  
  context = story.generate(request.args)

  return render_template("story.html", context=context)