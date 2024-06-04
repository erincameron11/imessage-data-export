# pip3 install Pillow # Not sure if necessary
# pip3 install tkcalendar # Not sure if necessary

# from tkinter import *
# from PIL import ImageTk, Image # for images
# from tkcalendar import *

# # ----- FUNCTIONS -----
# # Function: submit button handler
# def submit_handler():
#     # Use cal.get_date() to get the current date
#     start = start_date_cal.get_date()
#     end = end_date_cal.get_date()
#     print(start)
#     print(end)

# # ----- GUI -----
# # Create a tkinter root    
# root = Tk() # set the root of the GUI
# root.title("iMessage Extractor App")
# root.geometry("800x600") # Set the root dimensions

# # Create a logo image and place in the root
# logo = ImageTk.PhotoImage(Image.open("./images/bubble-download2.ico"))
# logo_label = Label(image=logo)
# logo_label.grid(row=0, column=0)

# # Create a title widget & place label in the root
# title = Label(root, text="iMessage Extractor")
# title.grid(row=0, column=1)

# # Create a Scrollbox to output previous export history

# # Create a Label to display a New Export subheading
# new_export = Label(root, text="New Export:")
# new_export.grid(row=1, column=0)

# # Create a Label to display the backup reminder
# backup_reminder = Label(root, text="**Reminder: Perform an unencrypted backup of your iPhone first**", foreground="red")
# backup_reminder.grid(row=2, column=1)

# # Create a Label to display a Dates subheading
# dates = Label(root, text="Dates:")
# dates.grid(row=3, column=0)

# # Create a Checkbox to select all dates


# # Create a Start Date calendar picker widget
# start_date_cal = Calendar(root, selectmode="day", year=2024, month=6, day=2, firstweekday="sunday", showweeknumbers=False, background="white", foreground="black", selectforeground="#4077FF")
# start_date_cal.grid(row=3, column=0)
# # Create a label for date output
# start_date_output = Label(root, text="Start Date: ", state=DISABLED)
# start_date_output.grid(row=3, column=0, pady=20)
# # Bind the calendar clicks to the label output
# start_date_cal.bind("<<CalendarSelected>>", lambda event: start_date_output.config(text="Start Date: " + start_date_cal.get_date()))

# # Create an End Date calendar picker
# end_date_cal = Calendar(root, selectmode="day", year=2024, month=6, day=2, firstweekday="sunday", showweeknumbers=False, background="white", foreground="black", selectforeground="#4077FF")
# end_date_cal.grid(row=3, column=1)
# # Create a label for date output
# end_date_output = Label(root, text="End Date: ", state=DISABLED)
# end_date_output.grid(row=3, column=1, pady=20)
# # Bind the calendar clicks to the label output
# end_date_cal.bind("<<CalendarSelected>>", lambda event: end_date_output.config(text="End Date: " + end_date_cal.get_date()))

# # Create a submit button and add to grid
# submit_btn = Button(root, text="Submit", padx=50, pady=8, command=submit_handler, fg="black", bg="#3366cc") # background bg not working
# submit_btn.grid(row=4, column=1)

# # Create an event loop
# root.mainloop()
















# --------------------- TESTING FRAMES & PACKING ---------------------

from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk, Image # for images
from tkcalendar import *

# ----- FUNCTIONS -----
# Function: submit button handler
def submit_handler():
    # Use cal.get_date() to get the dates
    start = start_date_cal.get_date()
    end = end_date_cal.get_date()
    print(start)
    print(end)

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
    

# ----- GUI -----
# Create a tkinter root    
root = Tk() # set the root of the GUI
root.title("iMessage Extractor App") # Set the title of the window
root.geometry("1000x700") # Set the root dimensions

# Create a frame for the entire program
main_frame = LabelFrame(root, width=800, height=600, borderwidth=0, highlightthickness=0, bg="gray")
main_frame.grid(row=0, column=0, padx=100, pady=15)

# Create a title frame and add a title - place above the content
title_frame = LabelFrame(main_frame, width=800, height=100, borderwidth=0, highlightthickness=0, bg="white")
title_frame.grid(row=1, column=0, padx=5, pady=5)
title = Label(title_frame, text="iMessage Extractor", font=("Arial", 35))
title.grid(row=1, column=0, padx=5, pady=5)

# Create a message frame inside the main frame
message_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
message_frame.grid(row=3, column=0, padx=5, pady=5)

# Create a Scrollbox to output previous export history
previous_export_scroll = scrolledtext.ScrolledText(message_frame, width=105, height=2, state=DISABLED) # FIX: width?
previous_export_scroll.grid(row=0, column=0, padx=5, pady=5)

# Create New Export subheading
new_export_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
new_export_frame.grid(row=4, column=0, padx=65, pady=5, sticky=W)
new_export = Label(new_export_frame, text="New Export:", font=("Arial", 20))
new_export.grid(row=0, column=0, padx=5, pady=5, sticky=W)
new_export_msg = Label(new_export_frame, text="** Reminder: Perform an unencrypted backup of your iPhone prior to exporting **", font=("Arial", 14), fg="red")
new_export_msg.grid(row=1, column=0, padx=5, pady=5)

# Create an All Dates checkbox
all_dates_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
all_dates_frame.grid(row=5, column=0, padx=65, pady=5, sticky=W)
all_dates_toggle = IntVar()
all_dates = Checkbutton(all_dates_frame, text="Download messages from all available dates", variable=all_dates_toggle, command=get_all_dates)
all_dates.grid(row=0, column=0, padx=5, pady=5, sticky=W)

# Create two calendar picker widgets
cal_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
cal_frame.grid(row=6, column=0, padx=5, pady=5)

# Start Date calendar picker
start_date_cal = Calendar(cal_frame, selectmode="day", year=2024, month=6, day=2, firstweekday="sunday", showweeknumbers=False, background="white", foreground="black", selectforeground="#4077FF")
start_date_cal.grid(row=0, column=0, padx=60)
# Create a label for date output
start_date_output = Label(cal_frame, text="Start Date: ", state=DISABLED)
start_date_output.grid(row=1, column=0, pady=20)
# Bind the calendar clicks to the label output
start_date_cal.bind("<<CalendarSelected>>", lambda event: start_date_output.config(text="Start Date: " + start_date_cal.get_date()))

# End Date calendar picker
end_date_cal = Calendar(cal_frame, selectmode="day", year=2024, month=6, day=2, firstweekday="sunday", showweeknumbers=False, background="white", foreground="black", selectforeground="#4077FF")
end_date_cal.grid(row=0, column=1, padx=60)
# Create a label for date output
end_date_output = Label(cal_frame, text="End Date: ", state=DISABLED)
end_date_output.grid(row=1, column=1, pady=20)
# Bind the calendar clicks to the label output
end_date_cal.bind("<<CalendarSelected>>", lambda event: end_date_output.config(text="End Date: " + end_date_cal.get_date()))



# test_frame = LabelFrame(main_frame, borderwidth=0, highlightthickness=0)
# test_frame.grid(row=6, column=0, padx=5, pady=5)
# t = Label(test_frame, text="ONE")
# t.grid(row=0, column=0)
# t2 = Label(test_frame, text="TWO")
# t2.grid(row=0, column=1)




# title_frame = LabelFrame(root, padx=340, pady=20, borderwidth=0, highlightthickness=0)
# title_frame.pack()

# # Create a logo image and place in the root
# logo = ImageTk.PhotoImage(Image.open("./images/bubble-download.png"))
# logo_label = Label(image=logo)
# # logo_label.grid(row=0, column=0)
# logo_label.pack()

# # Create a title widget & place label in the root
# title = Label(title_frame, text="iMessage Extractor")
# # title.grid(row=0, column=1)
# title.pack()

# Create a Scrollbox to output previous export history

# # Create a Label to display a New Export subheading
# new_export = Label(root, text="New Export:")
# new_export.grid(row=1, column=0)

# # Create a Label to display the backup reminder
# backup_reminder = Label(root, text="**Reminder: Perform an unencrypted backup of your iPhone first**", foreground="red")
# backup_reminder.grid(row=2, column=1)

# # Create a Label to display a Dates subheading
# dates = Label(root, text="Dates:")
# dates.grid(row=3, column=0)

# # Create a Checkbox to select all dates


# # Create a Start Date calendar picker widget
# start_date_cal = Calendar(root, selectmode="day", year=2024, month=6, day=2, firstweekday="sunday", showweeknumbers=False, background="white", foreground="black", selectforeground="#4077FF")
# start_date_cal.grid(row=3, column=0)
# # Create a label for date output
# start_date_output = Label(root, text="Start Date: ", state=DISABLED)
# start_date_output.grid(row=3, column=0, pady=20)
# # Bind the calendar clicks to the label output
# start_date_cal.bind("<<CalendarSelected>>", lambda event: start_date_output.config(text="Start Date: " + start_date_cal.get_date()))

# # Create an End Date calendar picker
# end_date_cal = Calendar(root, selectmode="day", year=2024, month=6, day=2, firstweekday="sunday", showweeknumbers=False, background="white", foreground="black", selectforeground="#4077FF")
# end_date_cal.grid(row=3, column=1)
# # Create a label for date output
# end_date_output = Label(root, text="End Date: ", state=DISABLED)
# end_date_output.grid(row=3, column=1, pady=20)
# # Bind the calendar clicks to the label output
# end_date_cal.bind("<<CalendarSelected>>", lambda event: end_date_output.config(text="End Date: " + end_date_cal.get_date()))

# # Create a submit button and add to grid
# submit_btn = Button(root, text="Submit", padx=50, pady=8, command=submit_handler, fg="black", bg="#3366cc") # background bg not working
# submit_btn.grid(row=4, column=1)

# Create an event loop
root.mainloop()