import psutil  # To get information on the process
import shutil # TO get number of high level operations on files
from network import * # User created module to check host and network connectivity


"""To check for the disk usage. Return False if the disk free space is less than 20%"""
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    du_free = du.free / du.total * 100
    return du_free > 20


'''Check for the cpu usage Notify User if the usage increases more than 75%'''
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage < 75


if not check_disk_usage('/') or not check_cpu_usage():
    print("Error!")
elif check_connectivity() and check_localhost():
    print('Everything Ok!')
else:
    print('Network connects Failed')
