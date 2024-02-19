# Event-Scheduler-System-using-Python-3.x-REST-APIs-and-Flask

This Python application is a simple event scheduler that allows users to manage and organize events. Built with Python 3.x, REST APIs, and Flask, the application supports basic CRUD operations (Create, Read, Update, Delete) for events. The data is stored in an SQLite database.

## Features:

* **Event Creation:** Users can create events by providing a title, description, start time, and end time.
* **Event Listing:** View all scheduled events in a sorted manner (earliest first).
* **Event Updating:** Modify details of existing events, such as changing time, title, or description.
* **Event Deletion:** Delete unwanted events.
* **Persistence:** Events are saved to an SQLite database, ensuring data is retained between sessions.

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
* Endpoint: /events/&lt;int:id&gt;
* Method: GET

**Update an Event**
* Endpoint: /events/&lt;int:id&gt;
* Method: PUT
* Parameters: title, start time, end time

**Delete an Event**
* Endpoint: /events/&lt;int:id&gt;
* Method: DELETE

Search for Events by Title
* Endpoint: /search?title=conference
* Method: GET
* Parameters: title
