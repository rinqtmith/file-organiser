import argparse
import os
import shutil

from pathlib import Path
from datetime import datetime

from file_types_config import FILE_TYPES


def move_file_to_folder(base_path, filename, file_path, dry_run, by_date):
    file_date = datetime.fromtimestamp(filename.stat().st_birthtime).date().isoformat()
    for file_type in FILE_TYPES:
        if filename.suffix.lower() in FILE_TYPES[file_type]:
            folder_path = file_path.joinpath(file_type)
            folder_date_path = (
                folder_path.joinpath(file_date) if by_date else folder_path
            )
            if dry_run:
                print(
                    f"[Dry Run] Would move {filename.name} to {folder_date_path.relative_to(base_path)} folder."
                )
            else:
                try:
                    os.makedirs(folder_date_path)
                except FileExistsError:
                    pass
                shutil.move(filename, folder_date_path.joinpath(filename.name))
            break
    else:
        other_path = file_path.joinpath("Others")
        other_date_path = other_path.joinpath(file_date) if by_date else other_path
        if dry_run:
            print(
                f"[Dry Run] Would move {filename.name} to {other_date_path.relative_to(base_path)} folder."
            )
        else:
            try:
                os.makedirs(other_date_path)
            except FileExistsError:
                pass
            shutil.move(filename, other_date_path.joinpath(filename.name))


def check_files(base_path, file_path, dry_run, by_date, recursive):
    for file_to_check in file_path.iterdir():
        if file_to_check.is_file():
            move_file_to_folder(base_path, file_to_check, file_path, dry_run, by_date)
        elif file_to_check.is_dir() and recursive:
            check_files(base_path, file_to_check, dry_run, by_date, recursive)
        else:
            print(f"Skipping {file_to_check.name} as recursive is not set.")


def main():
    parser = argparse.ArgumentParser(description="Organise files in a directory")
    parser.add_argument(
        "path", help="Path to the directory to organise files in", type=str
    )
    parser.add_argument(
        "--dry-run",
        help="Perform a dry run without making changes",
        action="store_true",
    )
    parser.add_argument(
        "-b", "--by-date", help="Organise files by date", action="store_true"
    )
    parser.add_argument(
        "-r", "--recursive", help="Organise files recursively", action="store_true"
    )
    parser.add_argument(
        "-a",
        "--recursive-all",
        help="Organise all files recursively",
        action="store_true",
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

    check_files(PATH, PATH, args.dry_run, args.by_date, args.recursive)


if __name__ == "__main__":
    main()
