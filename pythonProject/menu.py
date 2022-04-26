from package.bookcheckout import *
from package.bookreturn import *
from package.booksearch import *
from package.bookweed import *
from tkinter import *

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def clkOptions():
    clear_frames()
    options_frame.pack(fill="both", expand=1)

def clkCheckout():
    clear_frames()
    checkout_frame.pack(fill="both", expand=1)  # expands frame both horizontally and vertically


def clkReturn():
    clear_frames()
    return_frame.pack(fill="both", expand=1)


def clkSearch():
    clear_frames()
    search_frame.pack(fill="both", expand=1)


def clkData():
    clear_frames()
    data_frame.pack(fill="both", expand=1)
    plotGraph()

def clear_frames():
    checkout_frame.pack_forget()
    return_frame.pack_forget()
    search_frame.pack_forget()
    data_frame.pack_forget()
    options_frame.pack_forget()

def subCheckout():
    outcome = withdrawBook(bookID_entry.get(), memberID_entry.get())
    output_c.delete(0.0, END)
    output_c.insert(END, outcome)

def subReturn():
    outcome = returnBook(bookID_entry2.get())
    output_r.delete(0.0, END)
    output_r.insert(END, outcome)

def subSearch():
    outcome = searchBook(search_entry.get())
    output_s.delete(0.0, END)
    for result in outcome:
        output_s.insert(END, result.replace('_', ' ') + "\n")


def plotGraph():
    x, y = getData()

    plt.barh([5,5,3,8], y, align='center', label="Data 1")
    plt.legend()
    plt.ylabel("Books")
    plt.xlabel("Days since last return")
    plt.title("Most Unpopular Books")
    plt.show()


    #x_pos = [i for i, _ in enumerate(graphdata[0])]
    #plt.barh(x_pos, graphdata[1], color='green')
    #plt.ylabel("Books")
    #plt.xlabel("Days since last return")
    #plt.title("Most unpopular books")
    #plt.yticks(x_pos, graphdata[1])
    #plt.bar(graphdata[1], graphdata[0])
    #plt.show()

    #f = Figure(figsize=(5, 5), dpi=100)
    #a = f.add_subplot(111)
    #a.plot(graphdata)

    #canvas = FigureCanvasTkAgg(f, self)
    #canvas.show()
    #canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

window = Tk()
window.title("Library Program")
window.geometry("1200x600")
window.attributes("-fullscreen", True)

# options frame
options_frame = Frame(window, width=1200, height =600, bg="#262626")
Label(options_frame, text="Pick an option:", bg="#262626", fg="white", font="Ambit 40 bold").pack(pady=50)
buttonStyle = {'width': "28", 'font': "Ambit 28", 'bg': "#1A1A1A", 'fg': "white"}
btnCheckout = Button(options_frame, text="checkout", command=clkCheckout, **buttonStyle).pack(pady=12)
btnReturn = Button(options_frame, text="return", command=clkReturn, **buttonStyle).pack(pady=12)
btnSearch = Button(options_frame, text="search", command=clkSearch, **buttonStyle).pack(pady=12)
btnData = Button(options_frame, text="data", command=clkData, **buttonStyle).pack(pady=12)
btnExit = Button(options_frame, text="exit", command=exit, **buttonStyle).pack(pady=12)

# checkout frame
checkout_frame = Frame(window, width=1200, height=600, bg="#262626")
btnBack = Button(checkout_frame, text="back", command=clkOptions, **buttonStyle).pack(pady=12)
Label(checkout_frame, text="Enter book ID:", bg="#262626", fg="white", font="Ambit 32 bold").pack(pady=36)
bookID_entry = Entry(checkout_frame, width=16, font="Ambit 24 bold")
bookID_entry.pack(pady=(0,24))
Label(checkout_frame, text="Enter member ID:", bg="#262626", fg="white", font="Ambit 32 bold").pack(pady=36)
memberID_entry = Entry(checkout_frame, width=16, font="Ambit 24 bold")
memberID_entry.pack(pady=(0,24))
btnSubmit = Button(checkout_frame, text="submit", command=subCheckout, **buttonStyle).pack(pady=32)
output_c = Text(checkout_frame, width=28, height=2, fg= "white", bg="#262626", font="Ambit 32 bold", wrap=WORD)
output_c.pack()


# return frame
return_frame = Frame(window, width=1200, height=600, bg="#262626")
btnBack = Button(return_frame, text="back", command=clkOptions, **buttonStyle).pack(pady=12)
Label(return_frame, text="Enter book ID:", bg="#262626", fg="white", font="Ambit 32 bold").pack(pady=36)
bookID_entry2 = Entry(return_frame, width=16, font="Ambit 24 bold")
bookID_entry2.pack(pady=(0,24))
btnSubmit = Button(return_frame, text="submit", command=subReturn, **buttonStyle).pack(pady=32)
output_r = Text(return_frame, width=28, height=2, fg= "white", bg="#262626", font="Ambit 32 bold", wrap=WORD)
output_r.pack()


# search frame
search_frame = Frame(window, width=1200, height=600, bg="#262626")
btnBack = Button(search_frame, text="back", command=clkOptions, **buttonStyle).pack(pady=12)
Label(search_frame, text="Enter your search:", bg="#262626", fg="white", font="Ambit 32 bold").pack(pady=36)
search_entry = Entry(search_frame, width=16, font="Ambit 24 bold")
search_entry.pack(pady=(0,24))
btnSubmit = Button(search_frame, text="submit", command=subSearch, **buttonStyle).pack(pady=32)
output_s = Text(search_frame, width=28, height=10, fg= "white", bg="#262626", font="Ambit 32 bold", wrap=WORD)
output_s.pack()


# data frame
data_frame = Frame(window, width=1200, height=600, bg="#262626")
btnBack = Button(data_frame, text="back", command=clkOptions, **buttonStyle).pack(pady=12)


clkOptions()
window.mainloop()









if __name__ == '__main__':
    print("hi!!")
