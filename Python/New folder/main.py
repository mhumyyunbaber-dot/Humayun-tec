from flask import Flask, render_template,url_for

app = Flask(__name__)
posts = [
    {
        "author": "Allama",
        "title": "Book 1",
        "content": "Kash ful majub",
        "date": "20 1 2024",
    },
    {
        "author": "Allama Iqbal",
        "title": "Book 2",
        "content": "Kash majub",
        "date": "20 6 2024",
    }
]

@app.route("/")
@app.route("/<name>")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("About.html",title="About")

if __name__ == "__main__":
    app.run(debug=True)
