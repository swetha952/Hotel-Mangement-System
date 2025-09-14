
***

# 🌌 Celestial Oasis Inn – Hotel Booking System

A robust hotel management solution built with *Python* and *MySQL* to simplify room reservations, food service, activity scheduling, and billing.  
Celestial Oasis Inn features a streamlined command-line interface and secure database handling with environment-based configuration.

***

## 📖 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Setup & Usage](#-setup--usage)
- [Output](#-output)
- [File Structure](#-file-structure)
- [Security Guidelines](#-security-guidelines)
- [Future Enhancements](#-future-enhancements)
- [Contributors](#-contributors)
- [References](#-references)

***

## ✨ Features

- *Booking Details*: Register new customers with unique IDs and booking duration.
- *Booking Records*: Retrieve and view customer and booking details.
- *Room Reservation*: Choose from Single, Deluxe Double, or Presidential Suite with automatic availability checks.
- *Food Orders*: Add vegetarian or non-vegetarian meal plans per guest.
- *Activity Scheduling*: Book activities such as city tours, water sports, gym sessions, spa, and arcade games.
- *Automated Billing*: Generate consolidated bills including room rent, meals, and activities.
- *MySQL Integration*: Fast and reliable backend for bookings, orders, and invoices.
- *Secure Credentials*: All sensitive info managed through .env (never shared).
- *Cross-Platform*: Runs seamlessly on Windows, macOS, and Linux.

***

## 🛠️ Tech Stack

- Python 3.x
- MySQL
- mysql-connector-python
- python-dotenv (for environment variable management)

***

## 🚀 Setup & Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/swetha952/Hotel-Mangement-System.git
   cd Hotel-Mangement-System
   ```

2. **Install Dependencies**
   ```bash
   pip install mysql-connector-python python-dotenv
   ```

3. **Set up the MySQL Database**
   - Start your MySQL service.
   - Import schema and initial data:
     ```bash
     mysql -u your_mysql_user -p < "database_schema.sql"
     ```

4. **Configure Environment Variables**
   - Create a `.env` file with:
     ```
     DB_HOST=localhost
     DB_USER=your_mysql_user
     DB_PASS=your_mysql_password
     DB_NAME=celestial_oasis_inn
     ```
   - **Important:** Do not commit `.env` to version control.

5. **Launch the Application**
   ```bash
   python "HOTEL MANAGEMENT SYSTEM.py"
   ```

***

## 📷 Output (Sample)

- Confirmation messages for booking entries.
- Availability checks for rooms.
- Food and activity order summaries.
- Final consolidated bill with detailed breakdown.
- Error handling for invalid input or missing details.

***

## 🗂️ File Structure

```
Hotel-Mangement-System/
├── .gitignore
├── .env                 # Private, not committed
├── database_schema.sql   # Database schema
├── HOTEL MANAGEMENT SYSTEM.py   # Main application code
└── README.md             # This file
```

***

## 🔒 Security Guidelines

- `.env` must always be ignored by Git.
- Never upload real credentials or private configs.
- Provide a `.env.example` file with placeholder values for others to set up locally.

***

## 🔮 Future Enhancements

- *Cancellation & Refund Module*: Support for booking cancellations with refund rules.
- *Email & SMS Notifications*: Notify guests of booking confirmations, cancellations, and invoices.
- *Waitlist Management*: Auto-assign canceled rooms to waitlisted customers.
- *Analytics Dashboard*: Graphical insights into bookings, cancellations, and revenues.
- *Role-Based Access*: Separate logins for staff, admin, and management.

***

## 👥 Contributors

- Project developed for academic and learning purposes.
- Mentor: **Smt. Indrani Haridasan**
- Thanks to peers, teachers, and the open-source communities for support.

***

## 📚 References

- *Sumita Arora – Class XII*
- *NCERT Computer Science Textbook*
- Official documentation of Python & MySQL.

***

This perfectly matches the structure, spacing, and *section separator beauty* of the Propertease example!

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/83948908/e683469d-aaaa-48e9-b796-72ecfd27f0db/1000014940.jpg)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/83948908/100bd29b-e068-403d-ab5d-89feaab8ef01/1000014955.jpg)
