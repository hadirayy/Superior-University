class Item:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_info(self):
        print(f"title:{self.title}")
        print(f"author{self.author}")
class Book(Item):
    def __init__(self,title,author,pages):
        super().__init__(title,author)
        self.pages=pages
    def addtional_info(self):
        print(f"Pages:{self.pages}")
class Magazines(Item):
    def __init__(self,title,author,issue_number):
        super().__init__(title,author)
        self.issue_number=issue_number
    def addtional_info(self):
        print(f"Issue_nuumber:{self.issue_number}")
book=Book(2004,"Fearless",600)
book.display_info()
book.addtional_info()

magazine=Magazines("My_self","Stories",400)
magazine.display_info()
magazine.addtional_info()