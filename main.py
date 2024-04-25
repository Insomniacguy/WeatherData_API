# importing FLask class from flask library
from flask import Flask, render_template
import pandas as pd

# creating flask object / website object from  Flask class
app = Flask(__name__)

# variable = "Sip some chai and keep coding"
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


#  When the user visits home url home() is called. So route is connected to home().
# @ symbol means a decorator and it means it connects this method(route) to function home()
# However, to render the web-page tutorial.html flask needs a directory called "templates" with html file in it
@app.route("/")
def home():
    # var = "Sip some Chai"
    return render_template("home.html", data=stations.to_html())


# building end-points
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + f"{station.zfill(6)}" + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    print(station)
    print(type(station))
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + f"{station.zfill(6)}" + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    #  We want to return the entire data here for this file. In API we usually return a list or a dictionary.
    return df.to_dict(orient='records')


@app.route("/api/v1/yearly/<station>/<year>")
def yer_data(station, year):
    filename = "data_small/TG_STAID" + f"{station.zfill(6)}" + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    # temperature = df.loc[df['    DATE'].str.startswith(year)].to_dict(orient='records')
    temperature = df[df['    DATE'].str.startswith(year)].to_dict(orient='records')

    return {
        "station": station,
        "year": year,
        "temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True)
