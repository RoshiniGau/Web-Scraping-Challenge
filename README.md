# Web-Scraping-Challenge

# Background
 * This project is designed to show the latest data about Mars on a web page through the use of web scraping, MongoDB, and Flask.

# NASA Mars News
 * Scraped the NASA Mars News Site and collect the latest News Title and Paragraph Text.

# JPL Mars Space Images - Featured Image
 * Visit the url for JPL Featured Space Image and scrape to find the image url for the current Featured Mars Image and assigns to the url string of the full-size image.

# Mars Facts
 * Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
 * Use Pandas to convert the data to a HTML table string.
 
# Flask Application
  * Created a python script to run all of the scraping code and all of the scraped data was put into one Python Dictionary.
  * Created next, '/scrape' route which will import the Python script and call the scrape function.
  
 # MongoDB Application
  * A new database and collection was created .
  * Scraped data is stored in the database.
  * Created a root route which queried the Mongo database and passed the mars data into an HTML template to display the data.
 
 # HTML and BootStrap Application
  * Created an HTML file to display all of the data.