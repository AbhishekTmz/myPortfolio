# Import necessary modules
from flask import Flask, render_template
from project_data import projects  # Importing project data from external file
from skills import skills 
import os         # Importing skills data from external file

# Create the Flask application instance
app = Flask(__name__)

# Define the home route
@app.route("/")
def index():
    # Render the index.html template, passing in project and skills data
    return render_template("index.html", projects=projects, skills=skills)

# Define a dynamic route for individual project details
@app.route("/project/<project_name>")
def project_detail(project_name):
    # Get the specific project by name from the projects dictionary
    project = projects.get(project_name)
    
    # If the project exists, render the detail template
    if project:
        return render_template("project_detail.html", project=project)
    else:
        # If not found, return a simple message
        return "Project not found"

# Run the Flask development server
if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 4000))
    app.run(host="0.0.0.0" , port=port)