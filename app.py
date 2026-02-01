from flask import Flask, render_template, request

app = Flask(__name__)

FLAG = "FLAG{inspect_before_trust}"

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        if request.form.get("flag") == FLAG:
            return render_template("success.html")
        else:
            message = "❌ Wrong flag"

    return render_template("index.html", message=message)
