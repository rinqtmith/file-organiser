import argparse
import os
import shutil

from pathlib import Path
from datetime import datetime

from file_types_config import FILE_TYPES


def move_file_to_folder(base_path, filename, file_path, dry_run, by_date, r_all):
    file_date = datetime.fromtimestamp(filename.stat().st_birthtime).date().isoformat()
    for file_type in FILE_TYPES:
        if filename.suffix.lower() in FILE_TYPES[file_type]:
            folder_path = (
                base_path.joinpath(file_type)
                if r_all
                else file_path.joinpath(file_type)
            )
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
        other_path = (
            base_path.joinpath("Others") if r_all else file_path.joinpath("Others")
        )
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


def check_files(base_path, file_path, dry_run, by_date, recursive, r_all):
    for file_to_check in file_path.iterdir():
        if file_to_check.is_file():
            move_file_to_folder(
                base_path, file_to_check, file_path, dry_run, by_date, r_all
            )
        elif file_to_check.is_dir() and recursive:
            check_files(base_path, file_to_check, dry_run, by_date, recursive, r_all)
        else:
            print(f"Skipping {file_to_check.name} as recursive is not set.")


def remove_empty_folders(path, dry_run):
    for dirpath, dirnames, _ in os.walk(path, topdown=False):
        for dirname in dirnames:
            dir_to_check = Path(dirpath).joinpath(dirname)
            if dry_run:
                print(
                    f"Checking folder: {dir_to_check.relative_to(path)} would be removed if empty."
                )
            if not any(dir_to_check.iterdir()):
                if not dry_run:
                    os.rmdir(dir_to_check)


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

    check_files(
        PATH, PATH, args.dry_run, args.by_date, args.recursive, args.recursive_all
    )
    if args.recursive_all:
        remove_empty_folders(PATH, args.dry_run)


if __name__ == "__main__":
    main()
