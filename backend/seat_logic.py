import pandas as pd
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Sumanthreddy_8913",
        database="train_reservation"
    )

def allocate_seats(seats_requested):

    conn = get_connection()

    # ✅ Read seats into Pandas 😏🔥
    df = pd.read_sql("SELECT * FROM seats", conn)
s
    # ✅ Filter available seats
    available = df[df['status'] == 'available']

    # ✅ Group by row
    grouped = available.groupby('row_no')

    for row_no, seats in grouped:

        if len(seats) >= seats_requested:

            selected = seats.head(seats_requested)

            cursor = conn.cursor()

            for seat_id in selected['seat_id']:

                cursor.execute(
                    "UPDATE seats SET status='booked' WHERE seat_id=%s",
                    (int(seat_id),)
                )

            conn.commit()
            cursor.close()
            conn.close()

            return list(selected['seat_id'])

    conn.close()
    return []
