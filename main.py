from flask import Flask
from wae import os, model
app = Flask(__name__)

wae_model = None

@app.route("/") # loads homepage
def no_slug():
    return wae_model.load_index()

@app.route("/<slug>") # allows slug for the engine to process on the client's device
def main(slug):
    return wae_model.load_index()

@app.route("/pull", methods=["GET", "POST", "OPTIONS"])
def pull():
    wae_model.pull()
    return {}

if __name__ == "__main__":
    wae_model = model.Model("wae_config.json") # load static files for the project
    app.run(host="0.0.0.0", port=5000, debug=True)