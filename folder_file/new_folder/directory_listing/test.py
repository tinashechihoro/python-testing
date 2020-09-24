import unittest
import os
from pathlib import Path

from.list import DirectoryMapper

class MyTestCase(unittest.TestCase):


    def test_parent_directory_has_subdirectories(self):
        parent_directory = os.getcwd()
        self.assertEqual(parent_directory,Path.cwd())


    def test_parent_directory_has_files(self):
        dmapper = DirectoryMapper('.')
        files = dmapper.list_of_files()
        self.assertGreater(len(files),0)



    def test_sub_directories_has_files(self):
        dmapper = DirectoryMapper('.')
        files = dmapper.list_of_files()
        self.assertGreater(len(files), 0)

    def test_showing_all_files_in_parrent_directory(self):
        d = DirectoryMapper('.')
        all_files = d.list_file_and_directories()
        self.assertGreater(0, len(all_files))

    def test_showing_all_files_in_sub_directory(self):
        d = DirectoryMapper('.')
        all_files = d.list_file_and_directories()
        self.assertGreater(0,len(all_files))



    def test_path_is_a_directory(self):
        directory =  Path()
        d = DirectoryMapper('.')
        d.is_file(Path(d))






if __name__ == '__main__':
    unittest.main()
