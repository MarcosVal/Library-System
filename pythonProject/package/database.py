#if __name__ == "bookcheckout":
 #   directory = "database.txt"
##if __name__ == "menu" or "package.database":
    ##directory = "package/database.txt"
##else:
    ##directory = "database.txt"

def getNames():
    records = getBooks()

    names = []
    for book in records:
        if book[2] not in names:
            names.append(book[2])
    return names



def getBooks():
    records=[]
    print(__name__)
    f = open(directory, "r")
    for line in f:
        s = line.strip()
        book = s.split(":")
        records.append(book)
    f.close()
    return records

def isAvailable(bookID):
    records = getBooks()
    if records[int(bookID)-1][5]=="0":
        return True
    else:
        return False

def changeStatus(bookID, memberID=0):
    records = getBooks()

    targetRecord = records[bookID-1]
    oldRecord = (":").join(targetRecord)
    targetRecord[5] = str(memberID)
    updatedRecord= (":").join(targetRecord)

    f = open(directory, "r")
    updatedDatabase = f.read().replace(oldRecord, updatedRecord)
    f.close()

    f = open(directory, "w")
    f.write(updatedDatabase)
    f.close()


if __name__ == '__main__':
    directory = "../database.txt"
    print(getBooks())
elif __name__ == 'database':
    directory = "../database.txt"
else:
    directory = "./database.txt"



