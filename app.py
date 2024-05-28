from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/search', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        search = request.form["search"]
        return redirect(url_for("result", search=search))
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run()
