# iMessage Data Export

Exports iMessage and SMS chats, including videos and images, to local files for long-term storage.

# Tools and Technologies
* Python
    * `pandas` - for data framing
    * `os` - for file location lookup
    * `sqlite3` - for querying the database
* Jupyter

# Data Usage
* `service_name` used for colouring UI output of message bubbles as blue or green (iMessage/SMS)
* `date_delivered` used for getting the dates of messages sent
    * `pd.read_sql_query("SELECT datetime(message.date/1000000000 + strftime(\"%s\", \"2001-01-01\"),\"unixepoch\",\"localtime\") as Date FROM message", connection)`
* 