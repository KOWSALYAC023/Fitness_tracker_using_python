from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration
users = {
    "admin": "password123",
    "user": "mypassword"
}

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials. Please try again."
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
