from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'




def coordinates_to_address(latitude, longitude):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    if location:
        return location.raw['display_name']
    else:
        return "Address not found"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.json
        latitude = float(data["latitude"])
        longitude = float(data["longitude"])
        address = coordinates_to_address(latitude, longitude)
        return jsonify({"address": address})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

