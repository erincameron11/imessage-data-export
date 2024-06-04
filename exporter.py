# Main iMessage Data Export file for backing up iMessage chats, videos, and images

# ----- Imports -----
import sqlite3
import pandas as pd
import os # For 'chat.db' file location lookup

class Exporter:
    # ----- Initialize SQL connection -----
    # Lookup the full filepath to 'chat.db'
    file = os.path.abspath("chat.db")
    
    # Create a read-only connection to the database
    connection = sqlite3.connect(file, uri=True)
    
    # ----- Initialize DataFrames -----  
    # Select all columns and rows from chat table and initialize it into a dataframe
    chat_df = pd.read_sql_query("SELECT * FROM chat", connection)
    
    # Close the connection
    connection.commit()
    connection.close()

    # ----- Program Pseudocode -----
    # Create and display a UI
        # Display Last Backup Dates -  possibly create our own file on the computer to log this information
        # Date Start - calendar selector
        # Date End - calendar selector
        # Chats to Download - scrollbox with checkboxes next to each chat option
        # Download All Chats - checkbox
        # File Type for export - pdf, html, csv, etc?
        # Submit button
    # Get all the inputs from the user interface once the user selects "Submit"
        # Select messages from Date Start to Date End
        # Select only messages from particular contacts to download
        # Download each chat into their own file in the file type selected
        # Log the current date, Date Start, and Date End in the file/db we create to display in the future on the Display Last Backup Dates in the UI
    # 



    
    

        
        
    # Docstrings
   #  """Initializes the XXX for XXX
   #  Parameters
   #  ----------
   #  XXX : str
   #      Description
        
   #  Returns
   #  -------
   #  XXX : str
   #      Description
   # """

# Create an instance of our class and run the program
e = Exporter()
e.usingInitVariables()