from flask import Flask, request

app = Flask(__name__)


@app.route("/rce", methods=["GET", "POST"])
def rce():
    code = request.args.get("code")
    exec(code)
    return "Code executed."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
