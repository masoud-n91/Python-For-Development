from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route('/download-cv')
def download_cv():
    return send_from_directory(directory='static', path='pdf/CV.pdf', as_attachment=True)


@app.route("/register.html")
def register():
    return render_template("register.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/service.html")
def service():
    return render_template("service.html")


@app.route("/team.html")
def team():
    return render_template("team.html")


@app.route("/client.html")
def client():
    return render_template("client.html")


if __name__ == "__main__":
    app.run(debug=True)