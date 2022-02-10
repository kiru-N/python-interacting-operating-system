import os
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,"w") as file1:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  dt = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  date = dt.date()
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(date))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

