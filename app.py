from flask import Flask, flash, redirect, render_template, request, url_for

from forms import ContactForm, RegistrationForm
#initialize the Falsk app
app = Flask(__name__)

#load configurations settings
app.config["SECRET_KEY"] = "mysecretkey"  # Replace with a strong secret key

#define request handler method or function
@app.route("/")
def home():
       return render_template('home.html')
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/greetuser")
def hello_user():
    return render_template('index.html',username='sivaram')

@app.route("/greet")
def greet():
    return "<h2>Good morning</h2>"
@app.route("/products")
def product_list():
    products = ["Laptop","Smartphone", "Tablet"]
    return render_template("products.html", products=products)


# Route to display the contact form
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Route to handle form submission
@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    # Get data from the form
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Print data to console (for demonstration)
    print(f"Name: {name}, Email: {email}, Message: {message}")

    # Respond to the user
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


@app.route("/contact_wtf", methods=["GET", "POST"])
def contact_wtf():
       form = ContactForm()  # Initialize the form

       # Check if the form is submitted and valid
       if form.validate_on_submit():
           # Get form data
           name = form.name.data
           email = form.email.data

           # Process form data (e.g., print to console or save to database)
           print(f"Name: {name}, Email: {email}")
           flash("Your message has been received!", "success")

           # Redirect to avoid form re-submission
           return redirect(url_for("contact_wtf"))

       # Render the form with any validation errors
       return render_template("contact_form.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            # Handle successful form submission
            return redirect(url_for("welcome"))

        # Render the form with errors if validation fails
        return render_template("register.html", form=form)


#run the application
if __name__ == "__main__":
    app.run(debug=True)
    

