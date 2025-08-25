from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello from Flask on Azure App Service From Parteek Sandhey!"

@app.route("/about")
def about():
    return "This is a demo Python app deployed to Azure From Parteek Sandhey."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

