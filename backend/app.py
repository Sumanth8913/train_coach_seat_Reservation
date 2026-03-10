from flask import Flask, jsonify, request, render_template
import mysql.connector
from seat_logic import allocate_seats

app = Flask(__name__)

# ✅ DB Connection Helper 😏🔥
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Sumanthreddy_8913",
        database="train_reservation"
    )

# ✅ Home Page
@app.route("/")
def home():
    return render_template("BookTrains.html")

# ✅ View All Trains
@app.route("/view_trains")
def view_trains():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM trains")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

# ✅ Search Train by Number
@app.route("/search_train/<int:trainno>")
def search_train(trainno):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM trains WHERE trainno=%s", (trainno,))
    train = cursor.fetchone()

    cursor.close()
    conn.close()

    if not train:
        return jsonify({"status": "not_found"})

    train["status"] = "found"
    return jsonify(train)

# ✅ Trains Between Stations
@app.route("/trains_between/<fromstation>/<tostation>")
def trains_between(fromstation, tostation):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM trains WHERE fromstation=%s AND tostation=%s",
        (fromstation, tostation)
    )

    trains = cursor.fetchall()

    cursor.close()
    conn.close()

    if not trains:
        return jsonify({"status": "not_found"})

    return jsonify({
        "status": "found",
        "trains": trains
    })

# ✅ Fare Enquiry
@app.route("/fare_enquiry/<fromstation>/<tostation>")
def fare_enquiry(fromstation, tostation):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT fare FROM trains WHERE fromstation=%s AND tostation=%s",
        (fromstation, tostation)
    )

    train = cursor.fetchone()

    cursor.close()
    conn.close()

    if not train:
        return jsonify({"status": "not_found"})

    return jsonify({
        "status": "found",
        "fare": train["fare"]
    })

# ✅ Check Availability
@app.route("/check_availability/<int:trainno>")
def check_availability(trainno):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT available FROM trains WHERE trainno=%s", (trainno,))
    train = cursor.fetchone()

    cursor.close()
    conn.close()

    if not train:
        return jsonify({"status": "not_found"})

    return jsonify({
        "status": "found",
        "available": train["available"]
    })

# ✅ Add Train
@app.route("/add_train", methods=["POST"])
def add_train():

    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO trains (trainno, trainname, fromstation, tostation, available, fare)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        data["trainno"],
        data["trainname"],
        data["fromstation"],
        data["tostation"],
        data["available"],
        data["fare"]
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"status": "success"})

# ✅ Delete Train
@app.route("/delete_train/<int:trainno>", methods=["DELETE"])
def delete_train(trainno):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM trains WHERE trainno=%s", (trainno,))
    conn.commit()

    deleted = cursor.rowcount

    cursor.close()
    conn.close()

    if deleted:
        return jsonify({"status": "success"})

    return jsonify({"status": "fail"})

# ✅ Update Train
@app.route("/update_train", methods=["POST"])
def update_train():

    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE trains
    SET trainname=%s, fromstation=%s, tostation=%s,
        available=%s, fare=%s
    WHERE trainno=%s
    """

    values = (
        data["trainname"],
        data["fromstation"],
        data["tostation"],
        data["available"],
        data["fare"],
        data["trainnumber"]
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"status": "success"})

# ✅ Seat Allocation 😏🔥
@app.route("/book", methods=["POST"])
def book():

    if request.is_json:
        seats_requested = int(request.json["seats"])
    else:
        seats_requested = int(request.form["seats"])

    allocated = allocate_seats(seats_requested)

    return jsonify({
        "allocated_seats": allocated
    })

# ✅ User Login (Demo)
@app.route("/user_login", methods=["POST"])
def user_login():

    data = request.json

    if data["uname"] == "user@demo.com" and data["pword"] == "user":
        return jsonify({"status": "success"})

    return jsonify({"status": "fail"})

# ✅ User Registration (Demo)
@app.route("/register_user", methods=["POST"])
def register_user():

    data = request.json
    print(data)

    return jsonify({"status": "success"})

# ✅ Run App
if __name__ == "__main__":
    app.run(debug=True)
