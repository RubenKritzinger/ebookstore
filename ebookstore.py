import sqlite3

# Function to connect to the database


def database_connection():
    """Establish a connection to the SQLite database file."""
    connection = sqlite3.connect('ebookstore.db')
    cursor = connection.cursor()
    return connection, cursor

# Function to create the book table


def create_table(cursor):
    """Create a table named 'book' if it doesn't exist already."""
    cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        author TEXT,
                        qty INTEGER
                    )''')

# Function to add a new book to the database


def add_book(cursor, title, author, qty):
    """Insert a new book entry into the 'book' table."""
    cursor.execute(
        '''INSERT INTO book (title, author, qty) VALUES (?, ?, ?)''', (title, author, qty))

# Function to update book information


def update_book(cursor, book_id, title, author, qty):
    """Update the information of a book in the 'book' table based on book ID."""
    cursor.execute('''UPDATE book SET title=?, author=?, qty=? WHERE id=?''',(title, author, qty, book_id))

# Function to delete a book from the database


def delete_book(cursor, book_id):
    """Delete a book from the 'book' table based on book ID."""
    cursor.execute('''DELETE FROM book WHERE id=?''', (book_id,))

# Function to search for a specific book


def search_book(cursor, title):
    """Search for a book in the 'book' table based on title."""
    cursor.execute('''SELECT * FROM book WHERE title=?''', (title,))
    return cursor.fetchall()

# Function to display menu and handle user input


def display_menu():
    """Display the menu options for the user."""
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")

# Main function to run the program


def main():
    """Main function to run the program."""
    connection, cursor = database_connection()
    create_table(cursor)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            qty = int(input("Enter quantity: "))
            add_book(cursor, title, author, qty)
            connection.commit()
            print("Book added successfully!")
        elif choice == "2":
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            qty = int(input("Enter new quantity: "))
            update_book(cursor, book_id, title, author, qty)
            connection.commit()
            print("Book updated successfully!")
        elif choice == "3":
            book_id = int(input("Enter book ID to delete: "))
            delete_book(cursor, book_id)
            connection.commit()
            print("Book deleted successfully!")
        elif choice == "4":
            title = input("Enter title to search: ")
            result = search_book(cursor, title)
            if result:
                print("Book found:")
                for row in result:
                    print("ID:", row[0])
                    print("Title:", row[1])
                    print("Author:", row[2])
                    print("Quantity:", row[3])
            else:
                print("Book not found.")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()


if __name__ == "__main__":
    main()
