# train_coach_seat_Reservation
A full-stack Railway Train Coach Seat Reservation System built using HTML, CSS, JavaScript, Python (Flask), MySQL, and Pandas for seat allocation logic. The system allows users to search trains, check seat availability, book seats, and perform fare enquiries, with admin features for managing trains.


Below is ready-to-paste markdown.

🚆 Train Coach Seat Reservation System

A full-stack Railway Train Coach Seat Reservation System built using HTML, CSS, JavaScript, Python (Flask), MySQL, and Pandas.
This system allows users to search trains, check seat availability, book tickets, and perform fare enquiries, while admins can manage trains and schedules.

The project also implements smart seat allocation logic using Pandas, simulating real-world railway booking behavior.

⭐ Project Highlights

✔ Full-Stack Web Application
✔ Railway Seat Reservation Workflow
✔ Smart Seat Allocation using Pandas
✔ User + Admin Modules
✔ MySQL Database Integration
✔ REST API using Flask
✔ Responsive UI using HTML, CSS, JS

🧑‍💻 User Features

🔐 User Registration

🔑 User Login

🚆 View All Trains

🔎 Search Train by Train Number

📍 Trains Between Stations

💺 Seat Availability Check

💰 Fare Enquiry

🎟 Train Ticket Booking

👤 User Profile View

🔒 Change Password

🛠 Admin Features

🔐 Admin Login

➕ Add Train

✏ Update Train Details

❌ Delete Train

📋 View All Trains

🎟 Seat Allocation Logic

Seat booking uses Pandas DataFrame operations to simulate real train coach logic.

Algorithm:

1️⃣ Fetch seat data from MySQL
2️⃣ Filter seats where status = available
3️⃣ Group seats by row number
4️⃣ Allocate seats in the same row whenever possible
5️⃣ Update database seat status to booked

This ensures efficient and realistic seat allocation.

⚙️ Tech Stack
🌐 Frontend

HTML5
CSS3
JavaScript

🧠 Backend
Python
Flask Framework

🗄 Database
MySQL

📊 Data Processing
Pandas

📂 Project Structure
train_coach_seat_Reservation
│
├── backend
│   ├── app.py
│   ├── seat_logic.py
│
├── frontend
│   └── webcontent
│
│       ├── index.html
│       ├── UserLogin.html
│       ├── UserRegister.html
│       ├── UserHome.html
│       ├── UserViewTrains.html
│       ├── SearchTrains.html
│       ├── TrainBwStn.html
│       ├── Fare.html
│       ├── Availability.html
│       ├── BookTrains.html
│       ├── Payment.html
│       ├── AddTrains.html
│       ├── AdminHome.html
│       ├── AdminLogin.html
│       ├── AdminSearchTrain.html
│       ├── AdminUpdateTrain.html
│       ├── CancleTrain.html
│       ├── ViewTrains.html
│       ├── error.html
│       ├── UserHome_Css.css
│       
└── README.md
🗄 Database Configuration

Database Name:

train_reservation
Tables Used

users

id
email
password
firstname
lastname

trains

trainno
trainname
fromstation
tostation
available
fare

seats

seat_id
row_no
status

bookings

booking_id
user_id
trainno
seats_booked
booking_time

▶ How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/Sumanth8913/train_coach_seat_Reservation.git

2️⃣ Install Required Libraries
pip install flask
pip install mysql-connector-python
pip install pandas

3️⃣ Create Database
CREATE DATABASE train_reservation;

Then create tables for:

users
trains
seats
bookings

4️⃣ Run Backend Server

Navigate to backend folder:

cd backend

Run:

python app.py

Server will run at:

http://127.0.0.1:5000
📸 Project Screenshots

Example:

![Login Page](images/login.png)
![Train Booking](images/booktrain.png)

👨‍💻 Author
Sumanth Suram
🎓 B.Tech CSE Student
💻 Full-Stack Web Developer

GitHub
https://github.com/Sumanth8913
