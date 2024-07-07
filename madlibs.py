import random
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Load stories from JSON file
def load_stories():
    with open('stories.json', 'r') as file:
        return json.load(file)

# Route for the homepage
@app.route('/')
def index():
    stories = load_stories()
    selected_story = random.choice(stories)
    return render_template('index.html', story=selected_story['template'], words=selected_story['words'])

# Route to process user input and display the filled story
@app.route('/story', methods=['POST'])
def story():
    user_inputs = {key: request.form[key] for key in request.form}
    story_template = request.form['story_template']
    filled_story = story_template.format(**user_inputs)
    return render_template('story.html', story=filled_story)

if __name__ == '__main__':
    app.run(debug=True)
