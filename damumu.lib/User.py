from Book import Book # Book modülünün içindeki Book sınıfını içe aktar!!
class User:

    # Instance method to initialize user attributes. Works with object's own data.
    # Class method would use @classmethod decorator and take cls as first parameter.
    # Static method would use @staticmethod decorator and take anything as parameter.

      def __init__(self, username, password):
            self.username = username
            self.password = password
            self.books = []  
            self.incoming_requests = []

      def add_book(self, book):
            self.books.append(book)
            print(f"'{book.title}' added to {self.username}'s library.")
            # global library'den çıkart

      def list_books(self):
            if not self.books:
                  print(f"{self.username} has no books yet.")
            else:
                  print(f"{self.username}'s books:")
                  for b in self.books:
                        b.display()

      def remove_book(self, book_title):
            for b in self.books:
                  if b.title == book_title:
                        self.books.remove(b)
                        print(f"'{book_title}' removed from {self.username}'s library.")
                        return b
            print("book not found.")
            return None
      
      
      def receive_request(self, from_user, book_title):
            print(f"📚 {self.username} requested '{book_title}' from {from_user.username}.")
      
      def list_requests(self):
            if not self.incoming_requests:
                  print(f"{self.username} has no incoming requests.")
            else:
                  print(f"{self.username}'s coming requests:")
                  for req in self.incoming_requests:
                        print(f" - From {req[0]}: '{req[1]}'")
      @property
      def username(self):
            return self._username

      @username.setter
      def username(self, new_name):
            if len(new_name) < 2:
                  print("Username too short!")
            else:
                  self._username = new_name


if __name__ == "__main__":
      b1 = Book("the stranger", "albert camus", 1942)
      b2 = Book("crime and punishment", "fyodor dostoevsky", 1866)
      # print(b1.get_title) # prints the address in the memory.
      print(b1.title)

      user1 = User("damla", "1234")

      user1.add_book(b1)
      user1.add_book(b2)

      user1.list_books()

"""
LIST:
      Ordered, mutable, allows duplicate elements.
      Defined with square brackets []
      Example: my_list = [1, 2, 3, 4, 5]

TUPLE:
      Ordered, immutable, allows duplicate elements.
      Defined with parentheses ()
      Example: my_tuple = (1, 2, 3, 4, 5)

SET:
      Unordered, mutable, no duplicate elements.
      Defined with curly braces {}
      Example: my_set = {1, 2, 3, 4,5}

DICT:
      Unordered, mutable, key-value pairs, no duplicate keys.
      Defined with curly braces {}
      Example: my_dict = {'key1': 'value1', 'key2': 'value2'}

      Why use each?
      - Lists are great for ordered collections where duplicates are allowed.
      - Tuples are useful for fixed collections of items that shouldn't change.

      - Sets are ideal for collections of unique items and for set operations.
      - Dictionaries are perfect for key-value pair storage and fast lookups.
"""