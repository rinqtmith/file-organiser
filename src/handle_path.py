import sys


def handle_path(PATH, cwd):
    """
    Validate the provided path and its relationship to the current working directory.

    Args:
        PATH (Path): The path to validate.
        cwd (Path): The current working directory.

    Checks:
        - PATH exists and is a directory.
        - PATH is not relative to cwd.
        - cwd is not a subdirectory of PATH.

    Exits the program with an error message if any check fails.
    """
    if not PATH.exists():
        print(f"Path '{PATH}' does not exist.")
        sys.exit(1)

    if not PATH.is_dir():
        print(f"Path '{PATH}' is not a directory.")
        sys.exit(1)

    if PATH.is_relative_to(cwd):
        print(
            "Warning: The provided path is relative to the current working directory."
        )
        sys.exit(1)

    if cwd.is_relative_to(PATH):
        print(
            "Warning: The current working directory is a subdirectory of the provided path."
        )
        sys.exit(1)
