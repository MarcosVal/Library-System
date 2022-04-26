
def returnBook(bookID):
    records = getBooks()

    try:
        bookID = int(bookID)
    except ValueError:
        return "ID's must be integers."
    if bookID>len(records) or bookID<1:
        return "This ID is out of bounds."
    elif isAvailable(bookID):
        return "This book is already available!"
    else:
        changeStatus(bookID)
        logReturn(bookID)
        return "Book successfully returned!"
    
if __name__ == '__main__':
    from bookweed import logReturn
    from database import *

    print(returnBook(input("Return:")))
else:
    from .bookweed import logReturn
    from .database import *

