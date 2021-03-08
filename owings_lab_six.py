"""Owings Lab Six"""
from datetime import datetime, date
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


def time():
    """Time Function"""
    now_time = datetime.now()
    current_time = now_time.strftime("%H:%M:%S")
    return current_time


date_object = date.today()


@app.route("/")
def home():
    """Home Page Function"""
    with open('home.txt', 'r') as _f:
        return render_template("home.html",
                               plhld="Screenshot 2021-02-19 165624.png",
                               text=_f.read(),
                               title="Home",
                               time=time(),
                               date=date_object
                               )


@app.route("/beers")
def beers():
    """Beers Page Function"""
    with open('beer.txt', 'r') as _f:
        return render_template("home.html", plhld="Row-Of-British-Beers.png",
                               text=_f.read(),
                               title="Beer",
                               time=time(),
                               date=date_object
                               )


@app.route("/recipes")
def recipes():
    """Recipes Page Function"""
    with open('recipes.txt', 'r') as _f:
        return render_template("home.html", plhld="5F1A2766.jpg",
                               text=_f.read(),
                               title="Recipes",
                               time=time(),
                               date=date_object
                               )


@app.route("/conference")
def conference():
    """Conference Page Function"""
    thursday = pd.read_csv("THURSDAY_JUNE_18_2020.csv")
    friday = pd.read_csv("FRIDAY_JUNE_19_2020.csv")
    saturday = pd.read_csv("SATURDAY_JUNE_20_2020.csv")
    merged = pd.concat([thursday, friday, saturday])
    return render_template("home.html", plhld="82052.png",
                           text="""
<a href="https://www.homebrewcon.org/lineup/general-schedule/
"target="_blank"/rel="noopener noreferrer">
CLICK HERE for full Home Brew Con site</a>
                                """,
                           tables=merged.to_html(classes='merged',
                                                 header="true"),
                           title="Conference",
                           time=time(),
                           date=date_object
                           )


if __name__ == "__main__":
    app.run(debug=True)
