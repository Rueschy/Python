import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + '/testfolder/testfile.txt'

file = open(filename, 'r')

print(file.read())

file.close()
