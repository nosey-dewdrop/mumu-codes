from Library import Library
from Book import Book

library = Library()
damla = library.register("damla", "1234")
meltem = library.register("meltem", "5678")
library.print_users()

b1 = Book("dune", "frank Herbert", 1965)
damla.add_book(b1)
damla.list_books()

meltem.list_books()
