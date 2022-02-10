# Practice Notebook: Reading and Writing Files

"""Writing all the guest name in the file"""
guests = open('guests.txt',"w")
initial_guest = ['Bob','Andrea','Manuel','Sam']

for name in initial_guest:
    guests.write(name + "\n")

guests.close()


"""Append new guest list into file"""

new_guests = ['Daniel','Jacob','Polly','Khalid']

with open('guests.txt','a') as guests:
    for name in  new_guests:
        guests.write(name + '\n')


'''To remove the checked out names from the list '''
checked_out = ['Daniel', 'Jacob', 'Polly']
temp_list = []
# Get all the names from the file and store it in a temporary list
with open("guests.txt") as file1:
    temp_list = file1.readlines()


#Check whether the names are not in the checked out list and write it into a file
with open('guests.txt','w') as guests:
    for name in temp_list:
        if name.strip() not in checked_out:
            guests.write(name)

with open("guests.txt") as file1:
    for name in file1:
        print(name.strip())


