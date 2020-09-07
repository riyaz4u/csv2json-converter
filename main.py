from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfile
import os
import csv
import json

def openfile():
    file = askopenfilename(defaultextension=".csv",
                           filetypes=[("csv files", "*.csv")])
    if file == "":
        file = None
    else:
        fileEntry.delete(0, END)
        fileEntry.config(fg="blue")
        fileEntry.insert(0, file)
def convert(self):
    with open('data.csv') as csvfile:
       reader = csv.DictReader(csvfile)
       fieldnames = reader.fieldnames
       output = []
       for row in reader:
          j = {}
          for i, _ in enumerate(fieldnames):
             j[fieldnames[i]] = row[fieldnames[i]]
          output.append(j)
def save2json():
    with open('data.json','w') as jsonfile:
          jsonfile.write(json.dumps(output))
root = Tk()
root.geometry("600x350")
root.config(bg="light blue")
root.title("CSV Converter")
root.resizable(0, 0)

file = ""
defaultText = "\n\n\n\n\t\t Your extracted text will appear here.\n \t\t     you can modify that too."

appName = Label(root, text="CSV to JSON Converter ", font=('arial', 20, 'bold'),
                bg="light blue", fg='maroon')
appName.place(x=150, y=5)

labelFile = Label(root, text="Select csv File", font=('arial', 12, 'bold'))
labelFile.place(x=30, y=50)
fileEntry = Entry(root, font=('calibri', 12), width=40)
fileEntry.pack(ipadx=200, pady=50, padx=150)

csvFile = Button(root, text=" Open ", font=('arial', 12, 'bold'), width=30,
                        bg="sky blue", fg='green', command=openfile)
csvFile.place(x=150, y=80)

convert2json = Button(root, text="Read", font=('arial', 8, 'bold'),
                      bg="RED", fg='WHITE', width=20)
convert2json.place(x=250, y=120)

readcsv = Text(root, font=('calibri', 12), fg='light green', bg='black', width=60, height=30, bd=10)
readcsv.pack(padx=20, ipadx=20, pady=20, ipady=20)
readcsv.insert(INSERT, defaultText)
save2json = Button(root, text="Save to json File", font=('arial', 10, 'bold'),
                   bg="RED", fg='WHITE', command=save2json)
save2json.place(x=255, y=320)
if __name__ == "__main__":
    root.mainloop()