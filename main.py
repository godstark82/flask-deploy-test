from flask import Flask, render_template
from flask_frozen import Freezer  # Import Freezer

app = Flask(__name__)

# Define your routes
@app.route('/')
def hello():
    return render_template('index.html')

# Create a Freezer instance
freezer = Freezer(app)

# Main entry point to freeze or run the app
if __name__ == '__main__':
    app.run(debug=True)  # For development
