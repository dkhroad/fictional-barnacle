import os


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
    """

    # get list of directorys in the path
    # for each dir call find_file(...)
    dirs = []
    files = []
    subdir_files = []

    # why I chose scandir over listdir
    # https://www.python.org/dev/peps/pep-0471/
    with os.scandir(os.path.expanduser(path)) as it:
        for entry in it:
            if entry.is_dir():
                files.extend(find_files(suffix,entry.path))
            if entry.is_file() and entry.name.endswith(suffix):
                files.append(entry.path)

    return files


if __name__ == "__main__":
    files = find_files(".py","~/Work/udacity")
    for f in files:
        print(f)

