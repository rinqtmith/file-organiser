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

    for filename in file_list:
        if filename.is_file():
            for file_type in FILE_TYPES:
                if filename.suffix.lower() in FILE_TYPES[file_type]:
                    folder_path = PATH.joinpath(file_type)
                    try:
                        os.mkdir(folder_path)
                    except FileExistsError:
                        pass
                    shutil.move(filename, folder_path.joinpath(filename.name))
                    break
            else:
                other_path = PATH.joinpath("Other")
                try:
                    os.mkdir(other_path)
                except FileExistsError:
                    pass
                shutil.move(filename, other_path.joinpath(filename.name))


if __name__ == "__main__":
    main()
