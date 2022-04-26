
def withdrawBook(bookID, memberID):
    records = getBooks()

    try:
        bookID = int(bookID)
        test = int(memberID) # kept memberID as string to check length later on
    except ValueError:
        return "ID's must be integers."
    if bookID > len(records) or bookID < 1:
        return "Book ID is out of bounds."
    elif len(memberID) != 4:
        return "Member ID is out of bounds."
    elif not isAvailable(bookID):
        return "This book is not available!"
    else:
        changeStatus(bookID,memberID)
        logCheckout(bookID, records[bookID-1][2])
        return "Book successfully withdrawn!"

if __name__ == '__main__':
    from bookweed import logCheckout
    from database import *

    print(withdrawBook(input("Withdraw book:"), input("Member:")))
else:
    from .bookweed import logCheckout
    from .database import *