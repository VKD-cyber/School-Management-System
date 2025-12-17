# 🏫 Student School Management System  
![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

A **console-based School Management System** built using **Python and MySQL**.  
This project helps manage **students, teachers, attendance, fees, and salary records** efficiently using database connectivity.

---

## 📌 Project Overview
The **Student School Management System** is designed to automate basic school administration tasks.  
It uses **Python IDLE** connected to a **MySQL database** to perform CRUD operations such as inserting, deleting, updating, and displaying records.

---

## 🚀 Features
- ➕ Add student records  
- ❌ Remove student records  
- ➕ Add teacher records  
- ❌ Remove teacher records  
- 📅 Student attendance management  
- 👨‍🏫 Teacher attendance management  
- 💰 Student fee submission  
- 💵 Teacher salary payment tracking  
- 📋 Class-wise student display  
- 📄 Teacher list display  
- 🔐 Password-protected system  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Database:** MySQL  
- **Connector:** mysql-connector-python  
- **Interface:** Command Line (CLI)  
- **IDE:** Python IDLE  

---

## 🗂️ Database Tables
- `student`
- `teacher`
- `cattendance`
- `tattendance`
- `fees`
- `pay_salary`

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites
- Python 3.x  
- MySQL Server  

Install MySQL connector:
```bash
pip install mysql-connector-python

## Python and databas confriguation
con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="your_password",
    database="cs_project"
)
