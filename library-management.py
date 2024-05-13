class Book:
    def __init__(self, title, author, ISBN, genre, publication_date, availability):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre 
        self.publication_date = publication_date
        self.availability = availability
    
    def get_title(self):
        return self.title
    
    def set_title(self, new_title):
        self.title = new_title
    
    def get_author(self):
        return self.author
    
    def set_author(self, new_author):
        self.author = new_author
    
    def get_ISBN(self):
        return self.ISBN
    
    def set_ISBN(self, new_ISBN):
        self.ISBN = new_ISBN


class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id


class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography


class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category


def add_book(library):
    title = input("Enter title of book:")
    author = input("Enter book author:")
    isbn = input("Enter book ISBN:")
    genre = input("Enter book genre:")
    publication_date = input("Enter publication date:")
    availability = input("Enter availability:")
    library[isbn] = Book(title, author, isbn, genre, publication_date, availability)


def checkout_book(library, current_loans):
    isbn = input("Enter ISBN of the book:")
    user = input("Enter user name:")
    if isbn in library:
        current_loans[isbn] = user
        print(f"Book '{library[isbn].get_title()}' checked out to {user}.")
    else:
        print("Book not found.")


def checkin_book(library, current_loans):
    isbn = input("Enter ISBN of the book to return:")
    if isbn in current_loans:
        del current_loans[isbn]
        print(f"Book with ISBN {isbn} returned successfully.")
    else:
        print("Book not currently on loan.")


def display_books(library):
    print("Books in the library:")
    for isbn, book in library.items():
        print(f"ISBN: {isbn}, Title: {book.get_title()}, Author: {book.get_author()}")


def search_books(library):
    search_term = input("Enter search term (title or author):")
    found_books = []
    for isbn, book in library.items():
        if search_term.lower() in book.get_title().lower() or search_term.lower() in book.get_author().lower():
            found_books.append((isbn, book))
    if found_books:
        print("Found Books:")
        for isbn, book in found_books:
            print(f"ISBN: {isbn}, Title: {book.get_title()}, Author: {book.get_author()}")
    else:
        print("No books found.")


def add_user(library):
    name = input("Enter user's name:")
    library_id = input("Enter user's library ID:")
    library[name] = User(name, library_id)


def display_users(library):
    print("Users in the library:")
    for user_name, user in library.items():
        print(f"User: {user_name}, Library ID: {user.library_id}")


def add_author(library):
    name = input("Enter author's name:")
    biography = input("Enter author's biography:")
    library[name] = Author(name, biography)
    print("Author added successfully.")


def display_authors(library):
    print("Authors in the library:")
    for author_name, author in library.items():
        print(f"Author: {author_name}, Biography: {author.biography}")


def add_genre(library):
    name = input("Enter genre name:")
    description = input("Enter genre description:")
    category = input("Enter genre category:")
    library[name] = Genre(name, description, category)
    print("Genre added successfully.")


def display_genres(library):
    print("Genres in the library:")
    for genre_name, genre in library.items():
        print(f"Genre: {genre_name}, Description: {genre.description}, Category: {genre.category}")


def main():
    print("Welcome to the Library Management System")
    library = {}
    current_loans = {}
    
    while True:
        print("\n1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Exit")
        choice = input("Enter your choice:")
        
        if choice == "1":
            print("\n1. Add Book")
            print("2. Checkout Book")
            print("3. Checkin Book")
            print("4. Display Books")
            print("5. Search Books")
            book_choice = input("Enter your choice:")
            if book_choice == "1":
                add_book(library)
            elif book_choice == "2":
                checkout_book(library, current_loans)
            elif book_choice == "3":
                checkin_book(library, current_loans)
            elif book_choice == "4":
                display_books(library)
            elif book_choice == "5":
                search_books(library)
            else:
                print("Invalid choice.")
        elif choice == "2":
            print("\n1. Add User")
            print("2. Display Users")
            user_choice = input("Enter your choice:")
            if user_choice == "1":
                add_user(library)
            elif user_choice == "2":
                display_users(library)
            else:
                print("Invalid choice.")
        elif choice == "3":
            print("\n1. Add Author")
            print("2. Display Authors")
            author_choice = input("Enter your choice:")
            if author_choice == "1":
                add_author(library)
            elif author_choice == "2":
                display_authors(library)
            else:
                print("Invalid choice.")
        elif choice == "4":
            print("\n1. Add Genre")
            print("2. Display Genres")
            genre_choice = input("Enter your choice:")
            if genre_choice == "1":
                add_genre(library)
            elif genre_choice == "2":
                display_genres(library)
            else:
                print("Invalid choice.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
