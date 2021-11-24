import stat
import os
import subprocess
import sys
# This program is meant only to open files, but feel free to evolve it further


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# In this function replace the ******** with your path include your parent folder as well
# also this function will list the files inside the child folder
def findfile(name):
    c = r'\ '
    c = c.strip()
    name = c + name
    path = r'C:\Users\********\********\********' + name
    os.access(path, stat.S_IRWXU)
    subprocess.Popen('explorer ' + path)
    file_name = f"Opened {name} folder"
    print(file_name)
    files = os.listdir(r'C:\********\********\********\********' + name)
    print(files)


# here you can set the parent folder which contains other folders you want to open quickly
parent = r'C:\Users\********\********\********'
os.access(parent, stat.S_IREAD)
# this here will list the folders or files in your parent folder
orders = os.listdir(parent)
print('Where you can go:')
for i in orders:
    print(BColors.BOLD + i)
t = 1
while t == 1:
    order = input("Where you want to go? \n")
    order.strip()
    if order in orders:
        findfile(order)
    elif order == 'exit':
        exit()
    else:
        print("Put the exact name! or exit")
