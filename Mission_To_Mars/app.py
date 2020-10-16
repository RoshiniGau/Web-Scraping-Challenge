from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_costa

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data= mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function and save the results to a variable
    weather = scrape_costa.scrape_info()
    forecast={
        "min_temp":weather["min_temp"],
        "max_temp":weather["max_temp"]
    }
    # Update the Mongo database using update and upsert=True
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, forecast, upsert=True)


    # Redirect back to home page
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
