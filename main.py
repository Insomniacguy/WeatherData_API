# importing FLask class from flask library
from flask import Flask, render_template
import pandas as pd

# creating flask object / website object from  Flask class
app = Flask(__name__)


#  When the user visits home url home() is called. So route is connected to home().
# @ symbol means a decorator and it means it connects this method(route) to function home()
# However, to render the web-page tutorial.html flask needs a directory called "templates" with html file in it
@app.route("/")
def home():
    return render_template("home.html")


# building end-points
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True)
