# text.py
# It handles the work with text files (.txt)

def write(path: str, text: str):
    """write(path:str, text:str)
        Writes some text into a text file(.txt)
        path: full path of the file that we want to create
        text: the string that we want to write
    """
    try:
        with open(path, 'w') as f:
            f.write(text)
    except Exception as e:
        print("Exception thrown: {}".format(str(e)))


def read(path: str):
    """read_txt(path:str)->str
        Reads a text file and outputs its content.
        path: full path of the text file
    """
    try:
        with open(path, 'r') as f:
            result = f.read()
        return result
    except Exception as e:
        print("Exception thrown: {}".format(str(e)))


if __name__ == "__main__":
    pass
