import os


def list_entire_dir(path, what='all', types=[]):
    """
    Lists an entire directory (it searches inside subdirectories as well).

    input:
        path: Path of the directory
        what: What to search
            - 'all' for all the files and directories
            - 'dirs' only directories
            - 'files' only files
            Notice that for option 'files' we can also specify the types of the files
        types: Types of the files, ex.: ['.txt', '.py']
               If not specified, it will return all the files present in the dir.
    output:
        items : A list with the paths of files/of directories or both.
    """
    items = []
    for root, dirs, files in os.walk(path):
        if what == 'all':
            items.extend(os.path.join(root, dir) for dir in dirs)
            items.extend(os.path.join(root, file) for file in files)
        if what == 'dirs':
            items.extend(os.path.join(root, dir) for dir in dirs)
        if what == 'files':
            items.extend(os.path.join(root, file) for file in files)
            if types:
                items = [
                    file for file in items if filter_file(file, types)]

    return items


def filter_file(file, types):
    """
    This function checks if a file has the extension present in types.
    input:
        - file (string) the filepath of the file
        - types (list) the extensions to check for
            ex. ['.txt', '.py']
    output:
        bool (True/False)
    """
    for file_type in types:
        if file.lower().endswith(file_type):
            return True
    return False


if __name__ == "__main__":
    pass
