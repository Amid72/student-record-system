# student-record-system
A console-based Student Management System built with Python, OOP, and basic DSA. Supports adding, updating, deleting, viewing, searching, sorting students, and persistent storage using JSON. Demonstrates modular design and real-world programming concepts
# Student Management System
A **console-based Student Management System** built using **Python**, **OOPS**, and **basic DSA concepts**.  
This project demonstrates CRUD operations, data persistence using JSON, and clean modular design — perfect for portfolio and interview projects.
## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Folder Structure](#folder-structure)
5. [How to Run](#how-to-run)
6. [Sample Output](#sample-output)
7. [Future Improvements](#future-improvements)
8. [Interview Value](#interview-value)
## Project Overview
This project simulates a **school student management system** in Python.  
It allows users to **add, view, search, update, delete, and sort students** by their average marks.  
Student data is stored persistently in a **JSON file**, so information remains after program exit.

The system is built using **object-oriented programming (OOPS)** concepts and **basic data structures** like lists and dictionaries.


## Features
- **Add Student:** Add a new student with ID, name, age, and marks.  
- **View Students:** Display all students with details and average marks.  
- **Search Student:** Find a student by ID.  
- **Delete Student:** Remove a student by ID.  
- **Sort Students:** Sort students by average marks in descending order.  
- **Persistent Storage:** Data is saved in a JSON file and loaded on program start.  


## Tech Stack
- **Python 3.13**  
- **OOPS Concepts:** Class, Object, Constructor, Methods, Encapsulation  
- **Data Structures:** List of objects, Dictionary for storing student data  
- **File Handling:** JSON format for persistent storage  
- **Modular Code:** Separate files for student class, manager logic, storage, utilitie

## Folder Structure

student-management-system/
│
├── main.py # Program entry point, menu, and user input
├── student.py # Student class with attributes & methods (OOPS)
├── manager.py # CRUD logic: add, view, search, delete, sort
├── storage.py # Save & load student data from JSON
├── utils.py # Helper functions (input validation, formatting)
├── data.json # Student data (persistent storage)
└── README.md # Project documentation

yaml
Copy code


## How to Run
1. Clone or download the repo  
2. Make sure Python 3.13+ is installed  
3. Open terminal inside the project folder  
4. Run the program:

```bash
python main.py
Use the menu to interact:

Add students

View all students

Search, delete, or sort students

Data persists automatically in data.json

Sample Output
yaml
Copy code
--- Student Management System ---
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Sort Students by Average Marks
6. Exit
Enter your choice: 1

Enter student ID: 1
Enter name: Ravi
Enter age: 20
Enter marks (space separated): 80 90 85
Student added successfully.

Enter your choice: 2
ID: 1
Name: Ravi
Age: 20
Marks: [80, 90, 85]
Average: 85.00
--------------------
Future Improvements
Add update student functionality

Input validation & error handling improvements

Convert to FastAPI backend with REST API endpoints

Add a React frontend to make it full-stack

Advanced analytics: rank all students, class average, top performers

Interview Value
This project demonstrates:

Practical OOPS usage in Python

Implementing CRUD operations

File handling & JSON persistence

DSA fundamentals: list of objects, search, sort

Modular & clean code structure

You can confidently explain:

Class vs Object, Constructor, Methods

How file persistence works

How searching & sorting are implemented

How modules interact (main.py ↔ manager.py ↔ storage.py ↔ student.py)

yaml
Copy code

---

If you want, I can also **write the exact GitHub push commands** and **suggest a professional repo description + tags** so your project is **100% portfolio-ready**.  

Do you want me to do that next?






