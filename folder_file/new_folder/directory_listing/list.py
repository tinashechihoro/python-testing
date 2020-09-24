import os
from pathlib import Path


class DirectoryMapper(object):
    """
    With a path parameter give, the program will show all the directories
     and files from the current working directory
    """
    list_of_files = []
    path = ''

    def __init__(self, path):

        self.current_directory = os.getcwd()

    def is_directory(self, path):
        path = Path.is_dir(path)
        return True

    def is_file(self, path):
        """
        Check is a path is a file
        :param path:
        :return:
        """
        path = Path.is_file(path)
        return True

    def list_file_and_directories(self):

        for (directory_path, directory_names, filenames) in os.walk(self.current_directory):
            self.list_of_files += [os.path.join(directory_path, file) for file in filenames]

        return self.list_of_files

    def is_child_directory(self, list_of_files):
        for directory in list_of_files:
            directory = Path(directory)
            if self.is_directory(directory) and directory.parent():
                return True
            else:
                False



    def print_all_files_directories(self, all_list):
        for item in all_list:
            print(item)


# def directory_mapper(path):
#     directory = Path(path)
#     list_of_files = []
#     for (directory_path, directory_names, filenames) in os.walk(path):
#         list_of_files += [os.path.join(directory_path, file) for file in filenames]
#
#     print(list_of_files)


d = DirectoryMapper('.')

all_files = d.list_file_and_directories()

d.print_all_files_directories(all_files)
