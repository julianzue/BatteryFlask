from flask import Flask, render_template
import psutil
import time


app = Flask(__name__)


@app.route("/")
def home():

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged

    percent = "{:5.2f}".format(battery.percent)

    plugged = "Plugged In" if plugged else "Not Plugged In"

    date = time.strftime("%d.%m.%Y %H:%M:%S")

    return render_template("home.html", percent=percent, plugged=plugged, date=date)


if __name__ == "__main__":
    app.run(debug=True)