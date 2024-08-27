# Import the required csv module
import csv


# Define the main function
def main():
    # Initialize the books list
    books = []
    option = 0
    while option != 7:
        print("""
       Book Management Application:
       1. Add New Book
       2. Search Book by Title
       3. Sort Books by Title
       4. Find Oldest/Newest Book
       5. Export Book Titles to CSV File
       6. Extract Book Titles
       7. Exit
       """)

        try:
            option = int(input("Enter your choice: "))
            if option < 1 or option > 7:
                print("\nPlease select a valid option.\n")
        except ValueError:
            print("\nPlease enter a valid number.\n")

            # Call the corresponding function based on user input
        if option == 1:
            new_book = add_book()  # Add a new book
            if new_book:  # Check if the book is added successfully
                books.append(new_book)
        elif option == 2:
            search_title(books)  # Search for a book by title
        elif option == 3:
            sorted_books = sort_by_title(books)  # Sort books by title
            display_books(sorted_books)
        elif option == 4:
            find_oldest_newest(books)  # Find the oldest and newest books
        elif option == 5:
            export_to_csv(books)  # Export book titles to a CSV file
        elif option == 6:
            extract_titles(books)  # Extract book titles from the collection

    print("\nGoodbye! Hope to see you again.")


def add_book():
    print("Add New Book:")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    publication_year = int(input("Enter publication year: "))
    price = float(input("Enter book price: "))
    # create a tuple to store the book's data
    book = (title, author, genre, publication_year, price)
    return book


def search_title(books):
    search = input("Enter book title to search: ")
    for book in books:  # Iterate through each book in the list
        if book[
            0].lower() == search.lower():  # Compare book titles (case-insensitive)
            display_book(
                *book)  # Call display_book function to show the book details
            return
    print("\nBook not found.\n")


def sort_by_title(books):
    # Create a new list using sorted() function based on first element of sub-list
    sorted_books = sorted(books, key=lambda book: book[0].lower())
    return sorted_books


def display_books(books):
    print("\nBooks in Sorted Order:")
    for book in books:
        display_book(
            *book)  # Unpack the tuple and pass each element as an argument


def display_book(title, author, genre, publication_year, price):
    print(f"\nTitle: {title}")
    print(f"Author: {author}")
    print(f"Genre: {genre}")
    print(f"Publication Year: {publication_year}")
    print(f"Price: {price}\n")


def find_oldest_newest(books):
    if not books:
        print("\nNo books available.")
        return
    oldest = newest = books[0]  # Initialize with the first book
    for book in books[1:]:  # Iterate through the remaining books
        if book[3] < oldest[3]:  # Compare publication year
            oldest = book
        if book[3] > newest[3]:
            newest = book
    print("\nOldest Book:")
    display_book(*oldest)
    print("\nNewest Book:")
    display_book(*newest)


def export_to_csv(books):
    file_name = input("Enter CSV file name: ") + ".csv"
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Genre", "Publication Year",
                         "Price"])  # Write header
        for book in books:
            writer.writerow(book)  # Write book data as a row
    print(f"\nBook titles exported to {file_name}")


def extract_titles(books):
    print("\nBook Titles:")
    for book in books:
        print(book[0])


if __name__ == "__main__":  # Entry point of the program
    main()