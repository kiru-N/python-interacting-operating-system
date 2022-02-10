# To check all the files inside a directory is either a directory or file
path = os.getcwd()
folder = os.listdir(path)

def check_dir(dir_list):
    for names in dir_list:
        fullname = os.path.join(path,names)
        if os.path.isdir(fullname):
            check_dir(os.listdir(fullname))
            print(f'{fullname} is a directory')
        else:
            print(f'{fullname} is a file')

check_dir(folder)

