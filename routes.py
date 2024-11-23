from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the contact form
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit_contact", methods=["POST","GET"])
def submit_contact():
    # Retrieve data from the form
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Basic validation
    if not name or not email or not message:
        return "All fields are required.", 400  # 400 Bad Request

    # Process the data (for now, print it to the console)
    print(f"Name: {name}, Email: {email}, Message: {message}")

    # Respond with a confirmation message
    return f"Thank you, {name}. We have received your message."

@app.route("/search", methods=["GET", "POST"])
def search():
    # Check if the request method is GET
    if request.method == "GET":
        query = request.args.get("query")  # Get the search query from URL parameters
        if query:
            return f"Results for search query: {query}"
        return render_template("search.html")  # Display the form

    # If the method is POST, handle form submission
    if request.method == "POST":
        # Handle POST request logic here if needed
        return "POST method handling (currently unused)"
