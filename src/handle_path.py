import sys


def handle_path(PATH, cwd):
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
