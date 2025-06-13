import argparse


def parse_args():
    """
    Parse command-line arguments for the file organiser script.

    Returns:
        argparse.Namespace: Parsed command-line arguments with the following options:
            - path (str): Path to the directory to organise files in.
            - --dry-run (bool): Perform a dry run without making changes.
            - -b, --by-date (bool): Organise files by date.
            - -r, --recursive (bool): Organise files recursively.
            - -a, --recursive-all (bool): Organise all files recursively.
            - -v, --verbose (bool): Enable verbose output.
    """
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
