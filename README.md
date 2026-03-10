# 🚆 Train Coach Seat Reservation System

A full-stack Railway Train Coach Seat Reservation System built using **HTML**, **CSS**, **JavaScript**, **Python (Flask)**, **MySQL**, and **Pandas**. The system allows users to search trains, check seat availability, perform fare enquiries, and book tickets. Admin users can manage trains by adding, updating, and deleting train information.

---

## 🛠️ Technologies Used

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Database | MySQL |
| Data Processing | Pandas |

---

## 📁 Project Structure

```
train_coach_seat_Reservation
│
├── backend
│   ├── app.py
│   ├── seat_logic.py
│
├── frontend
│   └── webcontent
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
│       ├── forest.jpg
│       └── sandy.jpg
│
└── README.md
```

---

## ✨ Features

### 👤 User Features
- User Registration
- User Login
- View Trains
- Search Train by Number
- Trains Between Stations
- Seat Availability Check
- Fare Enquiry
- Train Booking
- User Profile
- Password Change

### 🔧 Admin Features
- Admin Login
- Add Train
- Update Train
- Delete Train
- View All Trains

---

## 🪑 Seat Allocation Logic

Seat allocation uses **Pandas DataFrame** operations.

**Steps:**
1. Load seat data from MySQL
2. Filter available seats
3. Group seats by row
4. Allocate seats from the same row when possible
5. Update database seat status to booked

---

## 🗄️ Database

**Database Name:** `train_reservation`

**Tables:**

| Table | Description |
|---|---|
| `users` | Stores registered user information |
| `trains` | Stores train details |
| `seats` | Stores seat layout and availability |
| `bookings` | Stores booking records |

**Create the database:**
```sql
CREATE DATABASE train_reservation;
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Sumanth8913/train_coach_seat_Reservation.git
cd train_coach_seat_Reservation
```

### 2. Install Dependencies
```bash
pip install flask
pip install mysql-connector-python
pip install pandas
```

### 3. Configure the Database
- Start your MySQL server
- Create the database:
```sql
CREATE DATABASE train_reservation;
```
- Update the database credentials in `backend/app.py` if needed

### 4. Run the Backend
```bash
cd backend
python app.py
```

### 5. Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 👨‍💻 Author

**Sumanth Suram**

[![GitHub](https://img.shields.io/badge/GitHub-Sumanth8913-181717?style=for-the-badge&logo=github)](https://github.com/Sumanth8913)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
