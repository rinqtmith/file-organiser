import argparse
import os
import shutil

from pathlib import Path

from file_types_config import FILE_TYPES


def main():
    parser = argparse.ArgumentParser(description="Organise files in a directory")
    parser.add_argument(
        "path", help="Path to the directory to organise files in", type=str
    )
    args = parser.parse_args()
    PATH = Path(args.path).resolve()
    cwd = Path.cwd()

    if not PATH.exists():
        print(f"Path '{PATH}' does not exist.")
        return

    if not PATH.is_dir():
        print(f"Path '{PATH}' is not a directory.")
        return

    if PATH.is_relative_to(cwd):
        print(
            "Warning: The provided path is relative to the current working directory."
        )
        return

    if cwd.is_relative_to(PATH):
        print(
            "Warning: The current working directory is a subdirectory of the provided path."
        )
        return

    file_list = list(PATH.iterdir())

    for filename in os.listdir(PATH):
        filename_path = PATH.joinpath(filename)
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
