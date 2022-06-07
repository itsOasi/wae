from flask import Flask
import os
import static.components.wae as wae
app = Flask(__name__)

@app.route("/")
def no_slug():
    return wae.output.load_index_page()

@app.route("/<slug>")
def main(slug):
    return wae.output.load_index_page()

@app.route("/pull", methods=["GET", "POST", "OPTIONS"])
def pull():
    repo = "https://github.com/itsOasi/portfolio.git"
    os.system(f"git pull {repo}")
    return {}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)