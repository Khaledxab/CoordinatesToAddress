from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

def coordinates_to_address(latitude, longitude):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    
    if location:
        address_details = {
            "address": location.raw['display_name'],
            "road": location.raw.get('address', {}).get('road', ''),
            "city": location.raw.get('address', {}).get('city', ''),
            "state": location.raw.get('address', {}).get('state', ''),
            "country": location.raw.get('address', {}).get('country', ''),
            "postcode": location.raw.get('address', {}).get('postcode', ''),
            "suburb": location.raw.get('address', {}).get('suburb', ''),
            "county": location.raw.get('address', {}).get('county', ''),
            "country_code": location.raw.get('address', {}).get('country_code', ''),
        }
        return address_details
    else:
        return {"error": "Address not found"}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.json
        latitude = float(data["latitude"])
        longitude = float(data["longitude"])
        address_details = coordinates_to_address(latitude, longitude)
        return jsonify(address_details)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
