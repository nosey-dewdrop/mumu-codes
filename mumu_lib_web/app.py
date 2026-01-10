from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "damla_mumu_secret"

# geçici user database (şimdilik memory)
users = {}

@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["user"] = username
            return redirect(url_for("home"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return render_template("register.html", error="Username exists")

        users[username] = {
        "password": password,
        "bio": "This user has no bio yet.",
        "followers": [],
        "following": [],
        "inbox": {},
        "reviews": [],
        "clubs": []
    }
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    username = session["user"]

    # user silinmişse logout yapılmış gibi davran
    if username not in users:
        session.clear()
        return redirect(url_for("login"))

    user = users[username]
    return render_template("home.html", user=user, username=username)

@app.route("/profile/<username>")
def profile(username):
    if username not in users:
        return "User not found", 404

    current = session.get("user")

    user = users[username]

    return render_template(
        "profile.html",
        user=user,
        username=username,
        current_user=current
    )
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "user" not in session:
        return redirect(url_for("login"))

    username = session["user"]
    user = users[username]

    if request.method == "POST":
        new_bio = request.form["bio"]
        users[username]["bio"] = new_bio
        return redirect(url_for("profile", username=username))

    return render_template("edit_profile.html", user=user, username=username)

@app.route("/messages")
def messages():
    if "user" not in session:
        return redirect(url_for("login"))
    
    username = session["user"]
    user = users[username]

    inbox = user["inbox"]  # dict: { "ada": [msg1, msg2], ... }

    return render_template("messages.html", inbox=inbox, username=username)


@app.route("/chat/<other>", methods=["GET", "POST"])
def chat(other):
    if "user" not in session:
        return redirect(url_for("login"))

    current = session["user"]

    if other not in users:
        return "User not found", 404

    # prevent messaging yourself
    if current == other:
        return "You cannot message yourself."

    # load message threads
    inbox = users[current]["inbox"].setdefault(other, [])
    other_inbox = users[other]["inbox"].setdefault(current, [])

    if request.method == "POST":
        msg = request.form["message"]
        # add message to both inboxes
        inbox.append({"from": current, "text": msg})
        other_inbox.append({"from": current, "text": msg})
        return redirect(url_for("chat", other=other))

    return render_template(
        "chat.html",
        current=current,
        other=other,
        messages=inbox
    )
    
if __name__ == "__main__":
    app.run(debug=True)