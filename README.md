# Event-Scheduler-System-using-Python-3.x-REST-APIs-and-Flask

This simple Flask application provides REST APIs to manage events. Users can add, view, update, delete events, and search for events by title.

## Prerequisites
- Python 3.x
- Flask

## Setup

1. Clone the repository:
2. Navigate to the project directory
3. Create a virtual environment: 
4. Install dependencies using '''pip install -r requirements.txt'''
5. Run the Flask application: '''flask run'''

## API Endpoints
**Get All Events**
* Endpoint: /events
* Method: GET

**Create a New Event**
* Endpoint: /events
* Method: POST
* Parameters: title, start time, end time

**Get a Single Event**
* Endpoint: /events/'<'int:id'>'
* Method: GET

**Update an Event**
* Endpoint: /events/'<'int:id'>'
* Method: PUT
* Parameters: title, start time, end time

**Delete an Event**
* Endpoint: /events/'<'int:id'>'
* Method: DELETE

Search for Events by Title
* Endpoint: /search?title=conference
* Method: GET
* Parameters: title
