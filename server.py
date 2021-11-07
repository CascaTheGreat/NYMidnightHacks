from flask import Flask
from flask import render_template
from flask import request
import model

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")
@app.route("/clicker")
def clicker():
  return render_template("clicker.html", matchUser = "@MaggieMoo")
@app.route("/signup", methods=["GET", "POST"])
def signup():
  return render_template("signup.html")
@app.route("/profile", methods=["GET","POST"])
def profile():
  if request.method == "POST":
    print(request.form)
    userList = model.output(request.form)
    return(render_template("profile.html", username = userList[0], user = userList[1], age = userList[2], bio = userList[3]))
  elif request.method == "GET":
    pass
@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
  jsdata = request.values
  model.marktime(jsdata)
  return False
if __name__ == "__main__":
  app.run()