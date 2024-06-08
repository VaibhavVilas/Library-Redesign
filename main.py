from book import BookManager
from user import UserManager
from check import CheckoutManager

# defining main menu function


def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Exit")

    # to take user's input
    choice = input("Enter choice: ")
    return choice

# defining main function


def main():
    try:
        # initializing all the necessary instances
        book_management = BookManager()
        user_management = UserManager()
        checkout_management = CheckoutManager(book_management, user_management)
    except Exception as e:
        print(f'Error initializing the system: {e}')
        return

    # to initialize the User Interface
    while True:
        try:
            choice = main_menu()

            # to add books
            if choice == '1':
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                isbn = input("Enter ISBN: ")
                book_management.add_book(title, author, isbn)

            # to display list of books
            elif choice == '2':
                book_management.list_books()

            # to add users
            elif choice == '3':
                name = input("Enter User Name: ")
                user_id = input("Enter User ID: ")
                user_management.add_user(name, user_id)

            # to make a checkout request
            elif choice == '4':
                user_id = input("Enter User ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                checkout_management.checkout_book(user_id, isbn)

            # to exit the interface
            elif choice == '5':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f'An error has occured : {e}')


# to run the script
if __name__ == "__main__":
    main()
