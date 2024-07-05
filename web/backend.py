from flask import Flask, render_template

app = Flask(__name__)
HOST = "localhost"
PORT = 8080

@app.route('/')
def main_menu():
    return render_template('index.html')


@app.route('/runtime')
def runtime():
    return render_template('runtime.html')


@app.route('/database')
def database():
    return render_template('database.html')

@app.route('/training')
def training():
    return render_template('training.html')


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
