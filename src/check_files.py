from src.move_file_to_folder import move_file_to_folder


def check_files(base_path, file_path, dry_run, by_date, recursive, r_all, verbose):
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
