# template of a single book
class Book:
    # defining attributes of a Book : title, author, isbn
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    # for Output
    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}'


# template of a single user
class User:
    # defining attributes of a User : name, user_id
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    # for Output
    def __str__(self):
        return f'User Name: {self.name}, User ID: {self.user_id}'


# template of a single checkout request
class Checkout:
    # defining attributes of a Checkout request : user_id, isbn
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

    # for Output
    def __str__(self):
        return f'User ID: {self.user_id}, ISBN: {self.isbn}'
