# Import the necessary packages
from src.helpers import dir, text, translateapi
import os
import argparse
from pprint import pprint


def args_parse():
    parser = argparse.ArgumentParser(
        description='Translates a string of characters or text files.')

    # Specifies what needs to be translated
    # It can be a directory path where .txt files are located,
    # Or a text file path,
    # Or a simple string of characters
    parser.add_argument('-t',
                        '--text',
                        type=str,
                        help='Text to be translated or path to a text file or \
                            directory which contains text files')

    # Specifies the language of the text that we want to be translated
    # If not specified, the program will try to detect the language
    parser.add_argument('-sl',
                        '--slang',
                        const='auto',
                        type=str, nargs='?',
                        default='auto',
                        help='Source language.')

    # Specifies the language in which we want to translate the text.
    # The default language is english ('en').
    parser.add_argument('-tl',
                        '--tlang',
                        const='en',
                        type=str, nargs='?',
                        default='en',
                        help='Target language.')

    # Specifies if we want to save the translations in the same
    # directory that was supplied. The files will have
    # "_translation" preffix.
    parser.add_argument('-s',
                        '--save',
                        const=False,
                        type=bool, nargs='?',
                        default=False,
                        help='Save translations as text files.')

    args = parser.parse_args()
    return args



def main():
    # Parse the cmd arguments
    args = args_parse()

    try:
        # Create a TranslateApi() object
        ob = translateapi.TranslateApi()

        # If a directory path was given as argument
        if os.path.isdir(args.text):
            print(
                "Translating all the text files from the directory\n{}...".format(args.text))
            text_files = dir.list_entire_dir(
                args.text,
                what='files',
                types=['.txt'])

            # Processes the text files
            for text_file in text_files:
                content = text.read(text_file)
                translation = ob.translate(content, args.slang, args.tlang)
                if args.save:
                    filename = text_file[text_file.rindex(
                        "\\") + 1:text_file.rindex(".")] + "_translation.txt"
                    filepath = text_file[:text_file.rindex("\\") + 1]
                    text.write((filepath + filename), translation)
                else:
                    print(f"File {text_file}:")
                    pprint(f"{content}", width=80)
                    print(f"Translation in {args.tlang} is:")
                    pprint(translation, width=80)
                    print('-' * 60)
            print("\nAll text files have been translated.")

        # If a text file path was given as argument
        elif os.path.isfile(args.text):
            print("File to translate")
            content = text.read(args.text)
            print(ob.translate(content, args.slang, args.tlang))

        # If a simple string was given as argument
        else:
            print(ob.translate(args.text, args.slang, args.tlang))

    except Exception as e:
        print(f"Exception thrown: {e}")


if __name__ == '__main__':
    main()
