from src.move_file_to_folder import move_file_to_folder


def check_files(base_path, file_path, dry_run, by_date, recursive, r_all, verbose):
    """
    Check and organise files in the specified directory.

    Args:
        base_path (Path): The root directory for organising files.
        file_path (Path): The current directory to check for files.
        dry_run (bool): If True, perform a dry run without making changes.
        by_date (bool): If True, organise files by date.
        recursive (bool): If True, process subdirectories recursively.
        r_all (bool): If True, apply recursive operation to all files.
        verbose (bool): If True, enable verbose output.

    Iterates over files and directories in file_path. Moves files using move_file_to_folder.
    If recursive is set, processes subdirectories recursively.
    """
    if verbose:
        print(f"Checking files in: {file_path}")
    for file_to_check in file_path.iterdir():
        if file_to_check.is_file():
            if verbose:
                print(f"Found file: {file_to_check.name}")
            move_file_to_folder(
                base_path, file_to_check, file_path, dry_run, by_date, r_all, verbose
            )
        elif file_to_check.is_dir() and recursive:
            if verbose:
                print(f"Found directory: {file_to_check.name}")
            check_files(
                base_path, file_to_check, dry_run, by_date, recursive, r_all, verbose
            )
        else:
            print(f"Skipping {file_to_check.name} as recursive is not set.")
