# Import necessary modules
from flask import Flask, render_template , request , jsonify
from project_data import projects  # Importing project data from external file
from skills import skills 
from ai_persona import AIPersona
import os         # Importing skills data from external file

# Create the Flask application instance
app = Flask(__name__)

ai_bot = AIPersona()
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

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    return jsonify({"response": ai_bot.get_response(user_input)})


# Run the Flask development server
if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 4000))
    app.run(host="0.0.0.0" , port=port)