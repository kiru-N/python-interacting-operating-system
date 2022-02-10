import os
import datetime as dt
print(os.remove('guest.txt')) # to remove the file
os.rename("guests.txt",'new_file.txt') # To rename the file
print(os.path.abspath('new_file.txt')) # to get the absolute path of the file

print(os.path.exists('new_file.txt')) # to check whether the path of the file exists
print(os.path.isfile('new_file.txt'))  # to check whether the file exists
print(os.path.getsize('new_file.txt'))  # To get the size of the file
timestamp = os.path.getctime('new_file.txt')  # File creation  Time
timestamp2 = os.path.getmtime('new_file.txt')

# to convert the unix timestamp to human readable timestamp
print(dt.datetime.fromtimestamp(timestamp))
print(dt.datetime.fromtimestamp(timestamp2))
# To get current working directory
print(os.getcwd())

# To create new directory
os.mkdir("new_dir")

# To remove directory
os.rmdir('new_dir')

# To change current directory to new_dir
os.chdir('new_dir')

# to list all files and folders inside directory
print(os.listdir("website"))

