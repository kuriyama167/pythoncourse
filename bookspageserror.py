class TooManyPagesReadError(ValueError):
    pass
class book: 
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def __repr__(self):
        return(f"<book{self.name}, read {self.page_read} page out of {self.page_count}>")
    
    def read(self, pages: int):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You Tried to read {self.page_read + pages} pages, but the book only has {self.page_count} pages."
            )
        
        self.page_read += pages
        print(f"You have now read {self.page_read} pages out of {self.page_count},")


my_book = book("The Great Gatsby", 180)
my_book.read(50)
my_book.read(1000)   

