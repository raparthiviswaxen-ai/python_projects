
from flask import Flask, render_template

# Create our Flask application
app = Flask(__name__)

# Create our homepage
@app.route("/")
def home():
    return render_template("index.html")


# Run our website
if __name__ == "__main__":
    app.run(debug=True)
