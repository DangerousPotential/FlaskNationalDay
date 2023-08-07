from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "POST":
    message = request.form['message'] #Dictionary
    with open('messages.txt', 'a') as file: # With Connection is automatically closed
      file.write(message + "\n") #file.write != file.append
    return render_template('index.html', message = message)
    with open('messages.txt', 'r') as file:
      posts = file.readlines()
    return render_template('index.html', posts = posts)


app.run(host='0.0.0.0', port=81)
