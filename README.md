# library_mangement_sys
A simple console-based library management system built using Python and PostgreSQL. This project allows users to add, view, update, and delete books from a PostgreSQL database.

# 📚 Library Management System using Python & PostgreSQL

Welcome to the **Library Management System** – a console-based application built with **Python** and **PostgreSQL**. It allows you to perform basic operations like adding, viewing, updating, and deleting books in a structured database.

## 🚀 Features

- ✅ **Add Book** – Insert new book records with title, author, year, and ISBN.
- 📖 **View Books** – Display all books stored in the PostgreSQL database.
- ✏️ **Update Book** – Edit details of a selected book using its ID.
- ❌ **Delete Book** – Remove a book record by its ID.
- 🔄 **Persistent Storage** – All data is saved using PostgreSQL for reliability.

## 🛠️ Tech Stack

- **Language**: Python 3
- **Database**: PostgreSQL
- **Library**: psycopg2

## ⚙️ How to Deploy

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/krishradadiya2525/library_management_sys.git
cd library_management_sys
```

### 2️⃣ Set Up the PostgreSQL Database

```sql
CREATE DATABASE library_sys;
```

### 3️⃣ Configure the Database in `library.py`

Edit the connection settings if needed:

```python
con = psycopg2.connect(
    dbname="library_sys",
    user="postgres",
    password="krish2525",
    host="localhost",
    port="5432"
)
```

### 4️⃣ Install Dependencies

```bash
pip install psycopg2

### 5️⃣ Run the Application

```bash
python3 library.py
```

## 📌 Future Enhancements

- Add GUI (Tkinter / PyQt)
- Implement search functionality
- Export book list to CSV
- Add user login system

## 🙋 Author

Made by "krish radadiya"
