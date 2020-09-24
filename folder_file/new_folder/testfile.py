import os
from pathlib import Path

def directory_mapper(path):
    directory = Path(path)
    list_of_files = []
    for(directory_path,directory_names,filenames) in os.walk(path):
        list_of_files  += [os.path.join(directory_path,file) for file in filenames ]

    print(list_of_files)


directory_mapper('/projects')