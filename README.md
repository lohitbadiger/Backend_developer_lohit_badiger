# Geocoding-Excel-Input-Output
<b>Problem statement</b><br>
1. Create a web service that allows users to upload an Excel sheet with an address field. One or more rows allowed. If not a web service, you can create a CLI interface.<br>
2. The system should use these address fields and using Google eocoding API, get the latitude and longitude of that address. <br>
3. The system then provides an excel download of the address excel ith latitude and longitude and formatted address fields.<br>
  <hr>
Choose a Excel file(.xlsx or .xls) with name of cities or countries in one column and resulting file will contain the latitute and longitude of cities in the second and third column.<br>
This application demonstates a simple Web Application based on [Django Framework 1.11](https://www.djangoproject.com/) of Python. The application uses  python3.0

## To run this app locally
1. Install Python3 : https://www.python.org/downloads/
2. Install pip for python <br>
`sudo apt-get update` <br>
`sudo apt-get install python-pip`
3. Install Virtual Environment <br>
`sudo pip install virtualenv`
4. Extract the Zip Folder and create Virtual Environment<br>
`virtualenv venv` <br>
5. Activate the Virtual Environment <br>
`source venv/bin/activate` <br>
`pip install -r requirements.txt` <br>
`python manage.py runserver` <br>
Open localhost on your browser  `127.0.0.1:8000` <br>

### Choose a File and Click the Upload Button, the required file with Longitude and Latitudes data will start download.

