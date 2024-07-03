from tkinter import *
from tkinter import filedialog

def submit():
    inputExcel = input_pathname.get()
    fileLocation = input_file_location.get()
    print(f"Pathname: {inputExcel}")
    print(f"File Location: {fileLocation}")

def openExcelFile():
    filepath = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
    if filepath:
        input_pathname.delete(0, END)
        input_pathname.insert(0, filepath)

def openFileLocation():
    filepath = filedialog.askopenfilename(filetypes=[('all files', '*.*')])
    if filepath:
        input_file_location.delete(0, END)
        input_file_location.insert(0, filepath)

window = Tk()

window.geometry("450x350")
window.title('SRA Automated Inspection Form Generator')

# Pathname entry and label
label_pathname = Label(window, text="Enter Pathname:")
label_pathname.pack(anchor='w', padx=10, pady=(20, 0))  # Padding for better positioning

input_pathname = Entry(window, width=50)
input_pathname.pack(padx=10, pady=5)  # Padding for better positioning

# Open button
open_Excel_file_button = Button(window, text="Open", command=openExcelFile)
open_Excel_file_button.pack(anchor='w', padx=10, pady=2)  # Padding for better positioning

# File Location entry and label
label_file_location = Label(window, text="File Location:")
label_file_location.pack(anchor='w', padx=10, pady=(20, 0))  # Padding for better positioning

input_file_location = Entry(window, width=50)
input_file_location.pack(padx=10, pady=5)  # Padding for better positioning

# Open button
open_file_button = Button(window, text="Open", command=openFileLocation)
open_file_button.pack(anchor='w', padx=10, pady=2)  # Padding for better positioning

# Submit button
submit_button = Button(window, text="Run", command=submit)
submit_button.pack(side=BOTTOM, pady=20)  # Padding for better positioning

window.mainloop()
