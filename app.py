from flask import Flask, render_template, request

app = Flask(__name__)

# Store flag securely (can move to env later)
FLAG = "FLAG{inspect_before_trust}"


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        submitted_flag = request.form.get("flag", "").strip()

        if submitted_flag == FLAG:
            return render_template("success.html")
        else:
            message = "❌ Wrong flag"

    return render_template("index.html", message=message)


# IMPORTANT:
# Do NOT run app.run() for cloud platforms.
# Gunicorn will automatically detect `app` object.
