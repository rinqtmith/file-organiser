import argparse

from pathlib import Path

from src.check_files import check_files
from src.remove_empty_folders import remove_empty_folders


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
    parser.add_argument(
        "-v", "--verbose", help="Enable verbose output", action="store_true"
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

    if args.verbose:
        print(f"Organising files in: {PATH}")
        print(f"with dry run: {args.dry_run}")
        print(f"by date: {args.by_date}")
        print(f"recursive: {args.recursive}")
        print(f"recursive all: {args.recursive_all}")
        print(f"Current working directory: {cwd}")
    check_files(
        PATH,
        PATH,
        args.dry_run,
        args.by_date,
        args.recursive,
        args.recursive_all,
        args.verbose,
    )
    if args.recursive_all:
        remove_empty_folders(PATH, args.dry_run, args.verbose)


if __name__ == "__main__":
    main()
