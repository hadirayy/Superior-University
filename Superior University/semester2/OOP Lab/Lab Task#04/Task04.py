class Book:
    def __init__(self,title,author,Publication_year):
        self.title= title
        self.author=author
        self.Publication_year=Publication_year
    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}, Publication_year:{self.Publication_year}"
my_book= Book("hopeless","Hadi",2004,)
print(my_book)