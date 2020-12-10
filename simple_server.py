from flask import Flask

app = Flask(__name__)
@app.route("/", methods = ["GET"])
def index():
	page = ""
    with open("index.html", "r") as rf:
        for line in rf.readlines():
            page += line + "\n"
    return page


if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "5000")
