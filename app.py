from flask import Flask, request, jsonify
import json
import sqlite3
app=Flask(__name__)

# Connecting to database created
def db_connector():
    conn=None
    try:
        conn=sqlite3.connect('events.sqlite')
    except sqlite3.error as e:
        print(e)

    return conn

#Function for reading and writing events from database
@app.route("/events", methods=['GET', 'POST'])
def events():
    conn=db_connector()
    cursor=conn.cursor()
    if request.method=="GET":
        cursor=conn.execute("SELECT * FROM events")
        List_of_events=[
            dict(id=row[0], title=row[1],start=row[2], end=row[3]) for row in cursor.fetchall()
        ]
        
        if List_of_events is not None:
            return jsonify(List_of_events)
        else:
            return jsonify({'error': 'There are no scheduled events'}), 404
        
    if request.method=="POST":
        Title=request.form['title']
        Start_Time=request.form['start time']
        End_Time=request.form['end time']
        sql="""INSERT INTO events (title, start, end) VALUES(?,?,?)"""

        cursor =cursor.execute(sql, (Title, Start_Time, End_Time))
        conn.commit()
        return jsonify({"message": f"Event created successfully with id: {cursor.lastrowid}"})
    
# Function for reading, writing and deleting any specific event with id.
@app.route("/event/<int:id>", methods=['GET','PUT',"DELETE"])
def single_event(id):
    conn=db_connector()
    cursor=conn.cursor()
    if request.method=='GET':
        cursor.execute("SELECT * FROM events WHERE id=?", (id,))
        rows=cursor.fetchall()
        for e in rows:
            event=e
            if event is not None:
                return jsonify(event), 200
            else:
                return jsonify({"message":"Something went wrong"})
    
    if request.method=='PUT':
        sql="""UPDATE events SET title=?, start=?, end=? WHERE id=?"""
        
        title=request.form["title"]
        Start_Time=request.form['start time']
        End_Time=request.form['end time']
        

        updated_event={
            'id':id,
            'title': title,
            'start time': Start_Time,
            'end time': End_Time
        }
        conn.execute(sql, (title, Start_Time,End_Time,id))
        conn.commit()
        return jsonify(updated_event)            
        
        
    if request.method=="DELETE":
        sql="""DELETE FROM events WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()      
        return jsonify({'error': f'Event with ID {id} has been deleted'}), 200

# Implementing search feature
@app.route("/search",methods=['GET'])
def search():
    # Implementing search feature
    if request.method == "GET":
        query_title = request.args.get('title')
        if query_title:
            conn=db_connector()
            cursor=conn.cursor()
            print(query_title)                
            cursor.execute("SELECT * FROM events WHERE title=?", (query_title,))
            rows=cursor.fetchall()
            if rows:
                # If rows are not empty, convert the result to a list of dictionaries
                events = []
                for row in rows:
                    event = {
                        'id': row[0],
                        'title': row[1],
                        'start time': row[2],
                        'end time': row[3]
                    }
                    events.append(event)

                return jsonify(events), 200
            else:
                return jsonify({"message": "No events found with the given title"}), 404


if __name__=="main":
    app.run(debug=True)