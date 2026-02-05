from flask import Flask, render_template, request
import os

app = Flask(__name__)

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


# 🔹 LOCALHOST SUPPORT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # cloud gives PORT, local uses 5000
    app.run(host="0.0.0.0", port=port, debug=True)
