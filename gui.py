# pip3 install Pillow # Not sure if necessary
# pip3 install tkcalendar # Not sure if necessary
# pip3 install tkmacosx # Not sure if necessary

from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from PIL import ImageTk, Image # for images
from tkcalendar import *
from tkmacosx import Button

# ----- FUNCTIONS -----
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

# ----- GUI -----
# Create a tkinter root    
root = Tk() # set the root of the GUI
root.title("iMessage Extractor App") # Set the title of the window
root.geometry("1000x800") # Set the root dimensions

# Create a frame for the entire program
main_frame = LabelFrame(root, width=1000, height=700, borderwidth=0, highlightthickness=0)
main_frame.pack(pady=15)
# main_frame.grid(row=0, column=0, padx=100, pady=15)

# Create a title frame and add a logo and title - place above the content
title_frame = LabelFrame(main_frame, width=800, height=100, borderwidth=0, highlightthickness=0, bg="white")
title_frame.grid(row=1, column=0, padx=5, pady=5)
logo = ImageTk.PhotoImage(Image.open("./images/bubble-download.ico"))
logo_label = Label(title_frame, image=logo)
logo_label.grid(row=1, column=0)
title = Label(title_frame, text="iMessage Extractor", font=("Arial", 35))
title.grid(row=1, column=1, padx=5, pady=5)

# Create a message frame inside the main frame with a Scrollbox to output previous export history
message_frame = LabelFrame(main_frame)
message_frame.grid(row=3, column=0, padx=5, pady=5)
previous_export_scroll = scrolledtext.ScrolledText(message_frame, width=97, height=1, bg="#ECECEC", wrap="word")
previous_export_scroll.grid(row=0, column=0, padx=5, pady=5)
# previous_export = Label(previous_export_scroll, text="Previous Export Dates: 2023-06-25 -> 2024-05-25, Chats Exported: Erin Cameron, Heather Kelly, Laura Richards, Jenny Applebottom", bg="#ECECEC", anchor='w')
previous_export_scroll.insert(INSERT, "Previous Export Dates: 2023-06-25 -> 2024-05-25\nChats Exported: Erin Cameron, Heather Kelly, Laura Richards, Jenny Applebottom")
previous_export_scroll.config(state=DISABLED) # Reset to disabled
# previous_export_scroll.window_create('end', window=previous_export)
# cb = Checkbutton(contacts_export_scroll, text=("first attempt"), bg="#ECECEC", anchor='w', cursor="arrow")
# previous_export_scroll.window_create('end', window=previous_export)
# previous_export_scroll.insert('end', '\n')

# Create New Export subheading with reminder text
new_export_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
new_export_frame.grid(row=4, column=0, pady=5, sticky=W)
new_export = Label(new_export_frame, text="New Export:", font=("Arial", 20))
new_export.grid(row=0, column=0, padx=5, pady=5, sticky=W)
new_export_msg = Label(new_export_frame, text="** Reminder: Perform an unencrypted backup of your iPhone prior to exporting **", font=("Arial", 14), fg="red")
new_export_msg.grid(row=1, column=0, padx=5, pady=5)

# Create an All Dates checkbox
all_dates_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
all_dates_frame.grid(row=5, column=0, pady=5, sticky=W)
dates_title = Label(all_dates_frame, text="Export Dates:", font=("Arial", 14))
dates_title.grid(row=0, column=0, sticky=W)
all_dates_toggle = IntVar()
all_dates = Checkbutton(all_dates_frame, text="Download messages from all available dates", variable=all_dates_toggle, command=get_all_dates)
all_dates.grid(row=1, column=0, padx=5, pady=5, sticky=W)

# Create two calendar picker widgets
cal_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
cal_frame.grid(row=6, column=0, padx=5, pady=5)

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
contacts_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
contacts_frame.grid(row=7, column=0, padx=5, pady=5)
contacts_title = Label(contacts_frame, text="Contacts to Download:", font=("Arial", 14))
contacts_title.grid(row=0, column=0, sticky=W)
all_contacts_toggle = IntVar()
all_contacts = Checkbutton(contacts_frame, text="ALL contacts", variable=all_contacts_toggle, command=get_all_contacts)
all_contacts.grid(row=1, column=0, padx=5, pady=5, sticky=W)
contacts_export_scroll = scrolledtext.ScrolledText(contacts_frame, width=97, height=2, bg="#ECECEC", state=DISABLED)
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
location_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
location_frame.grid(row=8, column=0, padx=5, pady=5, sticky=W)
location_title = Label(location_frame, text="Download location:", font=("Arial", 14))
location_title.grid(row=0, column=0, sticky=W)
download_location_label = Label(location_frame, text="")
download_location_label.grid(row=1, column=1)
location_btn = Button(location_frame, text="Download Location", padx=50, pady=8, foreground="black", background="#ECECEC", borderless=1, command=download_location)
location_btn.grid(row=1, column=0)

# Create a file output types dropdown selector
filetype_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
filetype_frame.grid(row=9, column=0, padx=5, pady=5, sticky=W)
filetype_title = Label(filetype_frame, text="Filetype:", font=("Arial", 14))
filetype_title.grid(row=0, column=0, sticky=W)
filetype_clicked = StringVar()
filetype_clicked.set("pdf")
filetype_dropdown = OptionMenu(filetype_frame, filetype_clicked, "pdf", "html", "csv")
filetype_dropdown.config(width=20)
filetype_dropdown.grid(row=1, column=0)

# Create a submit button and add to grid
button_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
button_frame.grid(row=10, column=0, sticky=E)
submit_btn = Button(button_frame, text="Submit", padx=50, pady=8, foreground="black", background="#adc2eb", borderless=1, command=submit_handler) # background bg not working
submit_btn.grid(row=0, column=0)

# Create an event loop
root.mainloop()