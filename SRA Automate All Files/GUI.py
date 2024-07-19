from tkinter import *
from tkinter import filedialog
from tkinter import ttk  
from data_entry import DataEntry

def submit():
    input_excel = input_pathname.get()
    pdf_file = input_pdf_file.get()
    output_dir = output_directory.get()
    
    progress_bar["value"] = 0  # Reset the progress bar
    result_message = data_entry_instance.process_data(input_excel, pdf_file, output_dir, progress_bar)

    if result_message == "Success":
        status_label.config(text="Reports generated successfully", fg="green")
    else:
        status_label.config(text=result_message, fg="red")

def openExcelFile():
    filepath = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
    if filepath:
        input_pathname.delete(0, END)
        input_pathname.insert(0, filepath)

def openPDFfile():
    default_file_path = 'PLUP Inspection Report.pdf'
    filepath = filedialog.askopenfilename(initialfile=default_file_path, filetypes=[('PDF files', '*.pdf')])
    if filepath:
        input_pdf_file.delete(0, END)
        input_pdf_file.insert(0, filepath)

def selectOutputDirectory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_directory.delete(0, END)
        output_directory.insert(0, folder_selected)

window = Tk()

img = PhotoImage(file='SRA_Logo_small.png')
window.iconphoto(False, img)

window.geometry("450x450")
window.title('SRA Automated Inspection Form Generator')

data_entry_instance = DataEntry()  # Create an instance of DataEntry

# Pathname entry and label
label_pathname = Label(window, text="Open Excel Spreadsheet (CSV file):")
label_pathname.pack(anchor='w', padx=10, pady=(20, 0))  # Padding for better positioning

input_pathname = Entry(window, width=50)
input_pathname.pack(padx=10, pady=5)  # Padding for better positioning

# Open button for Pathname
open_excel_file_button = Button(window, text="Open", command=openExcelFile)
open_excel_file_button.pack(anchor='w', padx=10, pady=2)  # Padding for better positioning

# PDF file entry and label
label_pdf_file = Label(window, text="Open Inspection Form (PDF file):")
label_pdf_file.pack(anchor='w', padx=10, pady=(20, 0))  # Padding for better positioning

input_pdf_file = Entry(window, width=50)
input_pdf_file.pack(padx=10, pady=5)  # Padding for better positioning

# Open button for PDF file
open_file_button = Button(window, text="Open", command=openPDFfile)
open_file_button.pack(anchor='w', padx=10, pady=2)  # Padding for better positioning

# Output Directory entry and label
label_output_directory = Label(window, text="Select File Location to Store:")
label_output_directory.pack(anchor='w', padx=10, pady=(20, 0))  # Padding for better positioning

output_directory = Entry(window, width=50)
output_directory.pack(padx=10, pady=5)  # Padding for better positioning

# Select button for Output Directory
select_output_button = Button(window, text="Select", command=selectOutputDirectory)
select_output_button.pack(anchor='w', padx=10, pady=2)  # Padding for better positioning

# Submit button
submit_button = Button(window, text="Run", command=submit)
submit_button.pack(side=BOTTOM, pady=20)  # Padding for better positioning

# Status label to display messages
status_label = Label(window, text="", fg="black")
status_label.pack(padx=10, pady=(10, 0))

# Progress bar
progress_bar = ttk.Progressbar(window, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(padx=10, pady=10)

window.mainloop()
