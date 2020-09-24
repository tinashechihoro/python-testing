"""
I have a folder and inside it I can put files and other sub folders containing files and so on so I can have recursive folders with files inside them

I want a way to pass the parent outermost folder name to a program and this program will recursively read out for me all the file names including those in nested folders and print them out
Could you think of a solution for that and implement a python program to do that in the most convenient way keeping in mind best practices

"""

import os


"""
Its assumed that the python script is running in the current folder
    Get user parent folder name
    
    get_parent_folder_name():
        folder_directory =  os.path
        assert
"""
def get_parent_folder(folder_name=''):

    parent_folder = os.getcwd()
    files_list = os.listdir(parent_folder)



    for file in files_list:

        print(file)



with open('deck.py','r') as f:
    contents = f.readlines()
    print(contents)
    f.close()



