from flask import Flask, render_template, request, redirect,flash

app = Flask(__name__, template_folder="templates")
app.secret_key = "Enter your app secret" #

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    email = request.form.get("email")
    password = request.form.get("password")
    c_password = request.form.get("c_password")
    
    if request.method == "GET":
        return render_template("signup.html", message="")
    else:
        pswrd = password.strip()
        c_pswrd = c_password.strip()
        if email.strip() == "":
            flash("Email field can't be empty!")
            return render_template("signup.html")
        # if pswrd == "" or c_pswrd == "":
        #     flash("Password can't be empty!")
        #     return render_template("signup.html", message="Password can't be empty!")
        if c_pswrd != pswrd:
            flash("Password doesn't match! Try again.")
            return render_template("signup.html")
        
        return redirect("/", 302)
            

@app.route("/auth/login")
def login():
    return render_template("login.html", message="")

@app.route("/about")
def about():
    pass

@app.route("/contact")
def contact():
    pass


if __name__ == "__main__":
    app.run(debug=True)