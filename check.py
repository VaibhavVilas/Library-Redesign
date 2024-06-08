from models import Checkout
from storage import Storage

# template of CheckoutManager to manage checkout requests


class CheckoutManager:

    # defining attributes for checkouts.json file where checkouts will be stored
    def __init__(self, book_manager, user_manager, file_path='checkouts.json'):
        self.file_path = file_path
        self.checkouts = self.load_checkouts()
        # attribute to access instance of BookManager,UserManager
        self.book_manager = book_manager
        self.user_manager = user_manager

    # method to load/read checkouts from checkouts.json
    def load_checkouts(self):
        checkouts_data = Storage.load_data(self.file_path)
        return [Checkout(**checkout) for checkout in checkouts_data]

    # method to save checkouts in checkouts.json
    def save_checkouts(self):
        checkouts_data = [checkout.__dict__ for checkout in self.checkouts]
        Storage.save_data(self.file_path, checkouts_data)

    # method to perform checkout of the book through isbn and user_id
    def checkout_book(self, user_id, isbn):

        # to check if the given user_id exists or not
        if not self.user_manager.is_user_present(user_id):
            print('\nUser not found. Please create an account first.')
            return

        # to check if given isbn(book) is available or not
        if self.book_manager.is_book_available(isbn):

            # appending the checkout request and saving it in checkouts.json
            checkout = Checkout(user_id, isbn)
            self.checkouts.append(checkout)
            self.save_checkouts()
            print('\nBook checked out.')
        else:
            print('\nBook not available for checkout.')
