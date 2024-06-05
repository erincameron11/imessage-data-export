# Installations -- Run if not already installed
# pip3 install Pillow
# pip3 install tkcalendar
# pip3 install tkmacosx

from tkinter import *
from tkinter import scrolledtext # for previous export history, and contact selection
from tkinter import filedialog # for destination folder selection
from PIL import ImageTk, Image # for logo
from tkcalendar import *
from tkmacosx import Button

# ---------- FUNCTIONS ----------
# Function: submit button handler
def submit_handler():
    # Use cal.get_date() to get the dates
    start = start_date_cal.get_date()
    end = end_date_cal.get_date()
    # Check that the start date is before the end date, and that all dates isn't selected
    if(start_date_cal.get_date() > end_date_cal.get_date() and all_dates_toggle.get() == 0):
        print("~~~start date cannot be before the end date")
        # Highlight the error and don't allow the user to download anything
    if(download_location_label.cget("text") == ""):
        print("~~~download location needs to be selected")
        # Highlight the error and don't allow the user to download anything
    # Get the filetype selected and do something with it
    filetype = filetype_clicked.get()
    print(filetype)
        
# Function: All Dates checkbox handler
def get_all_dates():
    if(all_dates_toggle.get() == 0):
        # Show the calendars
        end_date_cal.config(state=NORMAL)
        start_date_cal.config(state=NORMAL)
    else:
        # Hide the calendars
        end_date_cal.config(state=DISABLED)
        start_date_cal.config(state=DISABLED)
        start_date_output.config(text="Start Date: ALL")
        end_date_output.config(text="End Date: ALL")
        
# Function: All Contacts checkbox handler
def get_all_contacts():
    if(all_contacts_toggle.get() == 0):
        # Unselect all chats
        cb.deselect()
        cb2.deselect()
        cb3.deselect()
    else:
        # Select all chats
        cb.select()
        cb2.select()
        cb3.select()
        
# Function: Download Location dialog box handler
def download_location():
    root.filename = filedialog.askdirectory(initialdir="MacintoshHD", title="Select a Folder")
    download_location_label.config(text=root.filename)

# Function: Populate the previous export history section
def get_previous_export():
    # Locate the file to read previous export history from
    filename = "./Logs/logs.txt"
    # Loop through each line of the file and place into a list
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    # Remove the start and end dates
    start = lines.pop(0)
    end = lines.pop(0)
    # Display the output of start -> end dates, and chats exported
    previous_export_scroll.insert(INSERT, "Previous Export Dates: {start} -> {end}\n\nChats Exported: {chats}".format(start=start, end=end, chats=", ".join(lines)))
    # Set the field to disabled after inserting values
    previous_export_scroll.config(state=DISABLED)

    
# ---------- GUI ----------
# Create a tkinter root    
root = Tk() # set the root of the GUI
root.title("iMessage Extractor App") # Set the title of the window

# Set the root dimensions and center it in the screen
root.update_idletasks() #Add this line
width = 1200
height = 800
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Ensure the window is not resizable
root.resizable(False, False)

# Create a frame to hold the entire program
main_frame = LabelFrame(root, width=1000, height=700, borderwidth=0, highlightthickness=0)
main_frame.pack(pady=15)

# Create a title frame and add a logo and title - place above the content
title_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
title_frame.grid(row=1, column=0, padx=5, pady=5)
logo = ImageTk.PhotoImage(Image.open("./images/bubble-download.ico"))
logo_label = Label(title_frame, image=logo)
logo_label.grid(row=1, column=0)
title = Label(title_frame, text="iMessage Extractor", font=("Arial", 35))
title.grid(row=1, column=1, padx=5, pady=5)

# Create a message frame with a Scrollbox to output previous export history
message_frame = LabelFrame(main_frame, text="Previous Export History:", font=("Arial", 25))
message_frame.grid(row=3, column=0, padx=5, pady=5)
previous_export_scroll = scrolledtext.ScrolledText(message_frame, width=140, height=1, bg="#ECECEC", wrap="word")
previous_export_scroll.grid(row=0, column=0, padx=5, pady=5)
get_previous_export()

# Create a frame to hold all the new export content
content_frame = LabelFrame(main_frame, text="New Export: ", font=("Arial", 25))
content_frame.grid(row=4, column=0, padx=5, pady=10)

# Create New Export subheading with reminder text
new_export_frame = LabelFrame(content_frame, borderwidth=0, highlightthickness=0)
new_export_frame.grid(row=4, column=0, pady=5, sticky=W)
# new_export = Label(new_export_frame, text="New Export:", font=("Arial", 25))
# new_export.grid(row=0, column=0, padx=5, pady=5, sticky=W)
new_export_msg = Label(new_export_frame, text="** Reminder: Perform an unencrypted backup of your iPhone prior to exporting **", font=("Arial", 14, "italic"), fg="red")
new_export_msg.grid(row=1, column=0, padx=5, pady=5)

# Create an All Dates checkbox
all_dates_frame = LabelFrame(content_frame, borderwidth=0, highlightthickness=0)
all_dates_frame.grid(row=5, column=0, pady=5, sticky=W)
dates_title = Label(all_dates_frame, text="Export Dates:", font=("Arial", 18, "bold"))
dates_title.grid(row=0, column=0, sticky=W)
all_dates_toggle = IntVar()
all_dates = Checkbutton(all_dates_frame, text="Download messages from all available dates", variable=all_dates_toggle, command=get_all_dates)
all_dates.grid(row=1, column=0, padx=5, pady=5, sticky=W)

# Create two calendar picker widgets
cal_frame = LabelFrame(content_frame, borderwidth=0, highlightthickness=0)
cal_frame.grid(row=6, column=0, padx=5, pady=5, sticky=W)

# Start Date calendar picker
start_date_cal = Calendar(cal_frame, selectmode="day", year=2024, month=6, day=2, firstweekday="sunday", showweeknumbers=False, background="white", foreground="black", selectforeground="#4077FF")
start_date_cal.grid(row=0, column=0, padx=60)
# Create a label for date output
start_date_output = Label(cal_frame, text="Start Date: ", state=DISABLED)
start_date_output.grid(row=1, column=0, pady=5)
# Bind the calendar clicks to the label output
start_date_cal.bind("<<CalendarSelected>>", lambda event: start_date_output.config(text="Start Date: " + start_date_cal.get_date()))

# End Date calendar picker
end_date_cal = Calendar(cal_frame, selectmode="day", year=2024, month=6, day=2, firstweekday="sunday", showweeknumbers=False, background="white", foreground="black", selectforeground="#4077FF")
end_date_cal.grid(row=0, column=1, padx=60)
# Create a label for date output
end_date_output = Label(cal_frame, text="End Date: ", state=DISABLED)
end_date_output.grid(row=1, column=1, pady=5)
# Bind the calendar clicks to the label output
end_date_cal.bind("<<CalendarSelected>>", lambda event: end_date_output.config(text="End Date: " + end_date_cal.get_date()))

# Create a section for contacts to download
contacts_frame = LabelFrame(content_frame, borderwidth=0, highlightthickness=0)
contacts_frame.grid(row=7, column=0, padx=5, pady=5)
contacts_title = Label(contacts_frame, text="Contacts to Download:", font=("Arial", 18, "bold"))
contacts_title.grid(row=0, column=0, sticky=W)
all_contacts_toggle = IntVar()
all_contacts = Checkbutton(contacts_frame, text="ALL contacts", variable=all_contacts_toggle, command=get_all_contacts)
all_contacts.grid(row=1, column=0, padx=5, pady=5, sticky=W)
contacts_export_scroll = scrolledtext.ScrolledText(contacts_frame, width=140, height=2, bg="#ECECEC", state=DISABLED)
contacts_export_scroll.grid(row=2, column=0)
# TODO: FILL WITH CONTACT INFORMATION FOR EACH CONTACT IN THE CHAT DB
# for i in range(30):
#     cb = Checkbutton(contacts_export_scroll, text=(i+1), bg='white', anchor='w')
#     contacts_export_scroll.window_create('end', window=cb)
#     contacts_export_scroll.insert('end', '\n')
# TESTING
cb = Checkbutton(contacts_export_scroll, text=("first attempt"), bg="#ECECEC", anchor='w', cursor="arrow")
contacts_export_scroll.window_create('end', window=cb)
contacts_export_scroll.insert('end', '\n')
cb2 = Checkbutton(contacts_export_scroll, text=("second attempt"), bg="#ECECEC", anchor='w', cursor="arrow")
contacts_export_scroll.window_create('end', window=cb2)
contacts_export_scroll.insert('end', '\n')
cb3 = Checkbutton(contacts_export_scroll, text=("third attempt"), bg="#ECECEC", anchor='w', cursor="arrow")
contacts_export_scroll.window_create('end', window=cb3)
contacts_export_scroll.insert('end', '\n')

# Create a download location folder selector
location_frame = LabelFrame(content_frame, borderwidth=0, highlightthickness=0)
location_frame.grid(row=8, column=0, padx=5, pady=5, sticky=W)
location_title = Label(location_frame, text="Download Location:", font=("Arial", 18, "bold"))
location_title.grid(row=0, column=0, sticky=W)
download_location_label = Label(location_frame, text="")
download_location_label.grid(row=1, column=1)
location_btn = Button(location_frame, text="Download Location", padx=50, pady=8, foreground="black", background="#ECECEC", borderless=1, command=download_location)
location_btn.grid(row=1, column=0)

# Create a file output types dropdown selector
filetype_frame = LabelFrame(content_frame, borderwidth=0, highlightthickness=0)
filetype_frame.grid(row=9, column=0, padx=5, pady=5, sticky=W)
filetype_title = Label(filetype_frame, text="Filetype:", font=("Arial", 18, "bold"))
filetype_title.grid(row=0, column=0, sticky=W)
filetype_clicked = StringVar()
filetype_clicked.set("pdf")
filetype_dropdown = OptionMenu(filetype_frame, filetype_clicked, "pdf", "html", "csv")
filetype_dropdown.config(width=20)
filetype_dropdown.grid(row=1, column=0)

# Create a submit button and add to grid
button_frame = LabelFrame(content_frame, borderwidth=0, highlightthickness=0)
button_frame.grid(row=10, column=0, sticky=E)
submit_btn = Button(button_frame, text="Submit", padx=50, pady=8, foreground="black", background="#adc2eb", borderless=1, command=submit_handler) # background bg not working
submit_btn.grid(row=0, column=0)

# Create an event loop
root.mainloop()