import os
import glob

#
# files = os.listdir()
# folder_list  = []
# for file in files:
#     if 
#     print(file)#
# import glob
#
# for file_name in glob.iglob(directory_name=os.path.curdir(), recursive=True):
#     print(file_name)
# import os
# directories = os.listdir(path=os.curdir)
# print(directories)
import os

from folder_file.new_folder.testfile import directory_mapper

"""
search for files and directories from a given directory name
    or use the current location as the parent directory

    :param path: 
    :return: 
    """

all_files = list()

def get_list_of_files(path='.'):
    list_of_files =  os.listdir(path)

    for  entry in list_of_files:
        full_path = os.path.join(path,entry)

        if os.path.isdir(full_path):
            all_files =  all_files + get_list_of_files(full_path)


        else:
            all_files.append(full_path)

    return  all_files


import unittest
import os

os.walk()

class MyTestCase(unittest.TestCase):

    def test_path_is_set(self):
        path_isset = directory_mapper()
        self.assertEqual(True,)
    def test_something(self):

        self.assertEqual(True, False)

















