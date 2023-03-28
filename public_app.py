from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        response = requests.get(url)
        return f"Data processed: {get_all_titles(response.text)}"
    return render_template("index.html")


def get_all_titles(text: str) -> list:
    soup = BeautifulSoup(text, 'html.parser')
    h1_titles = [h1.text for h1 in soup.find_all('h1')]
    return h1_titles


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9191)
