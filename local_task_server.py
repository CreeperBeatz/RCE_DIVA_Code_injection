from flask import Flask, request

app = Flask(__name__)


@app.route("/rce", methods=["GET", "POST"])
def rce():
    code = request.args.get("code")
    exec(code)
    return "Code executed."

@app.route("/create-file", methods=["GET", "POST"])
def create_file():
    filename = request.args.get("filename")
    
    if filename:
        try:
            exec(f"with open('{filename}', 'w') as f: f.write('Hello RCE')")
            print("File created")
            return f"File {filename} created."
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "No filename provided."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
