from flask import Flask, render_template, request, json

app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(username, password)
        return json.jsonify({"result": "success"})


if __name__ == '__main__':
    app.run()
