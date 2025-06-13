import os

from pathlib import Path


def remove_empty_folders(path, dry_run, verbose):
    """
    Remove empty folders within the specified directory.

    Args:
        path (Path): The root directory to search for empty folders.
        dry_run (bool): If True, only print actions without making changes.
        verbose (bool): If True, print detailed output.

    Traverses the directory tree from the bottom up, checking each subdirectory.
    If a subdirectory is empty, it is removed (unless dry_run is True).
    """
    if verbose:
        print(f"Removing empty folders in: {path}")
    for dirpath, dirnames, _ in os.walk(path, topdown=False):
        if verbose:
            print(f"Checking directory: {dirpath}")
        for dirname in dirnames:
            if verbose:
                print(f"Checking subdirectory: {dirname}")
            dir_to_check = Path(dirpath).joinpath(dirname)
            if dry_run:
                print(
                    f"Checking folder: {dir_to_check.relative_to(path)} would be removed if empty."
                )
            if not any(dir_to_check.iterdir()):
                if not dry_run:
                    if verbose:
                        print(f"Removing empty folder: {dir_to_check}")
                    os.rmdir(dir_to_check)
