import os
import shutil

from file_types_config import FILE_TYPES

# use hard coded path for testing purposes
PATH = "../example_folder"


def main():
    for filename in os.listdir(PATH):
        filename_path = os.path.join(PATH, filename)
        if os.path.isfile(filename_path):
            _, ext = os.path.splitext(filename)
            for file_type in FILE_TYPES:
                if ext.lower() in FILE_TYPES[file_type]:
                    folder_path = os.path.join(PATH, file_type)
                    try:
                        os.mkdir(folder_path)
                    except FileExistsError:
                        pass
                    shutil.move(filename_path, folder_path)
                    break
            else:
                other_path = os.path.join(PATH, "Other")
                try:
                    os.mkdir(other_path)
                except FileExistsError:
                    pass
                shutil.move(filename_path, other_path)


if __name__ == "__main__":
    main()
