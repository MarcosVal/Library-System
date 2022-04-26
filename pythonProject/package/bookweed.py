from datetime import date, datetime

if __name__ == "menu":
    directory1 = "package/logfile.txt"
else:
    directory1 = "logfile.txt"

def getLogs():
    logs=[]
    f = open("../logfile.txt", "r")
    for line in f:
        log_line = line.strip().split(":")
        logs.append(log_line)
    f.close()
    return logs

def logCheckout(bookID, name):
    f = open("../logfile.txt", "a")
    f.write(str(bookID)+":"+name+":"+str(date.today())+":not_returned\n")
    f.close()

def logReturn(bookID):
    logs = getLogs()
    oldLog = ""
    updatedLog = ""
    for log_line in reversed(logs):
        if log_line[0] == str(bookID):
            oldLog = (":").join(log_line)
            log_line[3] = str(date.today())
            updatedLog = (":").join(log_line)
            break

    f = open("../logfile.txt", "r")
    updatedLogfile = f.read().replace(oldLog, updatedLog)
    f.close()

    f = open("../logfile.txt", "w")
    f.write(updatedLogfile)
    f.close()

def getData():
    records = getBooks()
    idleBooks = getNames()
    for book in records:
        if not isAvailable(book[0]) and book[2] in idleBooks:
            idleBooks.remove(book[2])

    logs = getLogs()

    lastCheckout = []
    for book in idleBooks:
        for log_line in reversed(logs):
            if log_line[1] == book:
                lastDate = datetime.strptime(log_line[3],'%Y-%m-%d')
                lastCheckout.append(int((datetime.today().year-lastDate.year)*12 + (datetime.today().month-lastDate.month)))
                break
    return [lastCheckout, idleBooks]



if __name__ == '__main__':
    from database import *
    print(getData())
else:
    from .database import *


