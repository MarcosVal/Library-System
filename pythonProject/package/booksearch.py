def searchBook(keyword):
    names = getNames()

    results=[]
    for search in names:
        if search.lower().count(keyword.lower()) != 0:
            results.append(search)
    return results


if __name__ == '__main__':
    from database import *

    print(searchBook(input("Search:")))
else:
    from .database import *
