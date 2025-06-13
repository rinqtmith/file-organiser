import argparse


def parse_args():
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

    return args
