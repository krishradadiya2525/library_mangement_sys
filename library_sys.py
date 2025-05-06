import psycopg2

# Connect to PostgreSQL
con = psycopg2.connect(
    dbname="library_sys",
    user="postgres",
    password="krish2525", 
    host="localhost",
    port="5432"
)
system = con.cursor()

# Create table
system.execute("""
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER,
    isbn TEXT
)
""")
con.commit()

# Functions
def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter year: "))
    isbn = input("Enter ISBN: ")
    system.execute("INSERT INTO books (title, author, year, isbn) VALUES (%s, %s, %s, %s)",
                   (title, author, year, isbn))
    con.commit()
    print("Book added successfully.")

def view_books():
    system.execute("SELECT * FROM books")
    for book in system.fetchall():
        print(book)

def delete_book():
    bookid = int(input("Enter Book ID to delete: "))
    system.execute("DELETE FROM books WHERE id = %s", (bookid,))
    con.commit()
    print("Book deleted.")

def update_book():
    bookid = int(input("Enter Book ID to update: "))
    title = input("Enter new title: ")
    author = input("Enter new author: ")
    year = int(input("Enter new year: "))
    isbn = input("Enter new ISBN: ")
    system.execute("UPDATE books SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s",
                   (title, author, year, isbn, bookid))
    con.commit()
    print("Book updated.")

# Menu
while True:
    print("\n!!! Library Menu !!!")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice--> ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("***Exiting program***")
        break
    else:
        print("Invalid choice. Try again.")

# Close connection
con.close()
