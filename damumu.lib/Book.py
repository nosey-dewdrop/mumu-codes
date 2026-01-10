class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"* {self.title} by {self.author} ({self.year})")

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def year(self):
        return self._year
    
    @title.setter
    def title(self, new_title):
            if len(new_title) < 2:
                  print("title too short!")
            else:
                  self._title = new_title

    @author.setter   
    def author(self, new_author):
            if len(new_author) < 2:
                  print("author name too short!")
            else:
                  self._author = new_author

    @year.setter
    def year(self, new_year):
            if new_year < 0:
                  print("year cannot be negative!")
            else:
                  self._year = new_year

            