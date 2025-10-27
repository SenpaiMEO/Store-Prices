class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn          # Private
        self.available = True

    
    def get_isbn(self):   # Getter for ISBN
        return self.__isbn

     
    def set_isbn(self, new_isbn):  # Setter for ISBN
        if isinstance(new_isbn, str) and len(new_isbn) > 0:
            self.__isbn = new_isbn

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, Status: {status}")


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id  # Private
        self.borrowed_books = []

    
    def get_membership_id(self): # Getter
        return self.__membership_id

    def set_membership_id(self, new_id):     # Setter
        if isinstance(new_id, str):
            self.__membership_id = new_id

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow this book.")


class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, title, author, isbn):
        new_book = Book(title, author, isbn)
        library.books.append(new_book)
        print(f"Staff {self.name} added '{title}' to the library.")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        print(f"Member {member.name} added to {self.name}.")

    def show_all_books(self):
        print(f"\n--- Books in {self.name} ---")
        if self.books:
            for book in self.books:
                book.display_info()
        else:
            print("No books in the library.")


if __name__ == "__main__":
    library = Library("City Library")

    book1 = Book("Python", "Omar", "123-456")
    book2 = Book("Data Science", "Essam", "789-012")

    library.books.extend([book1, book2])

    member1 = Member("Mahmoud", "M001")
    staff1 = StaffMember("Saif", "S001", "ST001")

    # Add members
    library.add_member(member1)
    library.add_member(staff1)

    # Show books
    library.show_all_books()

    # Member borrows book
    member1.borrow_book(book1)

    # Staff adds a new book
    staff1.add_book(library, "AI Basics", "Dr. AI", "555-666")

    # Show updated library
    library.show_all_books()

    # Member returns book
    member1.return_book(book1)

    # Try to access private ISBN directly (will fail)
    # print(book1.__isbn)  # AttributeError
    print(f"ISBN via getter: {book1.get_isbn()}")  # Works