import os
import sys

def find_files(suffix,path="."):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths

    Time Complexity: O(d*n) where d is the number of directories and n 
    is the number of files in each directory. 
    """


    # why I chose scandir over listdir
    # https://www.python.org/dev/peps/pep-0471/
    try:
        with os.scandir(os.path.expanduser(path)) as it:
            for entry in it:
                if entry.is_dir():
                    for dir in find_files(suffix,entry.path):
                        yield dir
                elif entry.is_file() and entry.name.endswith(suffix):
                    yield entry.path
    except PermissionError as exc:
        pass



if __name__ == "__main__":
    for files in find_files(".py","~"):
        print(files)

