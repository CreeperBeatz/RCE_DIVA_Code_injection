from flask import Flask, render_template, request, redirect, url_for, session
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = "your_secret_key"

def get_all_titles(text: str) -> str:
    soup = BeautifulSoup(text, 'html.parser')
    h2_titles = [h2.text for h2 in soup.find_all('h2')]

    # Create an HTML table from the titles
    table_html = "<table><thead><tr><th>Title</th></tr></thead><tbody>"
    for title in h2_titles:
        table_html += f"<tr><td>{title}</td></tr>"
    table_html += "</tbody></table>"
    return table_html

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        response = requests.get(url)
        titles = get_all_titles(response.text)
        session['titles'] = titles
        return redirect(url_for('results'))
    return render_template("index.html")

@app.route("/results")
def results():
    titles = session.get('titles', None)
    if titles:
        return render_template("results.html", titles=titles)
    else:
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9191)
