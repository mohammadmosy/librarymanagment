import json
import os

FILENAME = "books.json"

# Create a file if it does not exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        json.dump([], f)

# Upload books
def load_books():
    with open(FILENAME, "r") as f:
        return json.load(f)

#Save books
def save_books(books):
    with open(FILENAME, "w") as f:
        json.dump(books, f, indent=4)

# Add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book name: ")
    number = input("Enter Number of books: ")

    books = load_books()

    books.append({
        "title": title,
        "author": author,
        "number": number
    })

    save_books(books)
    print("Book added successfully!")

# Delete book
def delete_book():
    title = input("Enter title of the book to delete: ")
    books = load_books()

    updated_books = [book for book in books if book["title"] != title]

    if len(updated_books) == len(books):
        print("Book not found.")
    else:
        save_books(updated_books)
        print("Book deleted successfully.")

# Show books
def list_books():
    books = load_books()
    if not books:
        print("No books found.")
        return

    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['number']})")

# Main menu
def main():
    while True:

        choice = input("1. List books\n2. Add book\n3. Delete book\nchoice:>")
        match choice:
            case"1":
                list_books()
            case"2":
                add_book()

            case"3":
                delete_book()

          


"""main()"""