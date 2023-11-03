from flask import Flask,render_template,send_file

app = Flask(__name__,static_url_path="/resume")

@app.route("/")
def index():
    return render_template("index.html")


