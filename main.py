from pathlib import Path

from src.arg_parser import parse_args
from src.check_files import check_files
from src.handle_path import handle_path
from src.remove_empty_folders import remove_empty_folders


def main():
    args = parse_args()
    PATH = Path(args.path).resolve()
    cwd = Path.cwd()

    handle_path(PATH, cwd)

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
