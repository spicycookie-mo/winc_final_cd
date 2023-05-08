# Import what we need from flask
from flask import Flask, render_template

# Create a Flask app inside `app`
app = Flask(__name__)

# Define a dictionary of animals and their sounds
animals = {
    'cow': 'MOoooOo!',
    'sheep': 'Baaaah!',
    'pig': 'Oink oink!',
	'dog': 'Bark!'
}

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    # Render the index template and pass in the animals dictionary
    return render_template('index.html', animals=animals)

# Assign a function to be called when the path `/animal/<animal_name>` is requested
@app.route('/animal/<animal_name>')
def animal(animal_name):
    # Look up the sound for the requested animal
    sound = animals.get(animal_name)
    # If the animal is not found, return a 404 error
    if not sound:
        return 'Animal not found', 404
    # Render the animal template and pass in the animal name and sound
    return render_template('animal.html', animal_name=animal_name, sound=sound)
