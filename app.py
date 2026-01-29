from flask import Flask, render_template
import requests
from config import NASA_API_KEY

app = Flask(__name__)

@app.route("/")
def index():
    url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={NASA_API_KEY}"
    data = requests.get(url).json()

    asteroids = []
    for date in data["near_earth_objects"]:
        asteroids.extend(data["near_earth_objects"][date])

    return render_template("index.html", asteroids=asteroids)

@app.route("/asteroid/<asteroid_id>")
def asteroid_detail(asteroid_id):
    url = f"https://api.nasa.gov/neo/rest/v1/neo/{asteroid_id}?api_key={NASA_API_KEY}"
    asteroid = requests.get(url).json()
    return render_template("asteroid.html", asteroid=asteroid)

if __name__ == "__main__":
    app.run(debug=True)
