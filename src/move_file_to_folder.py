import os
import shutil

from datetime import datetime

from file_types_config import FILE_TYPES


def move_file_to_folder(
    base_path, filename, file_path, dry_run, by_date, r_all, verbose
):
    """
    Move a file to an appropriate folder based on its type and date.

    Args:
        base_path (Path): The root directory for organising files.
        filename (Path): The file to be moved.
        file_path (Path): The current directory of the file.
        dry_run (bool): If True, only print actions without making changes.
        by_date (bool): If True, organise files into date-based subfolders.
        r_all (bool): If True, use base_path for all moves; otherwise, use file_path.
        verbose (bool): If True, print detailed output.

    The function determines the file type and moves the file into a corresponding
    folder (and optionally a date subfolder). If the file type is not recognised,
    it is moved to an "Others" folder. Handles folder creation and supports dry run mode.
    """
    if verbose:
        print(f"Processing file: {filename.name}")
    file_date = datetime.fromtimestamp(filename.stat().st_birthtime).date().isoformat()
    for file_type in FILE_TYPES:
        if filename.suffix.lower() in FILE_TYPES[file_type]:
            if verbose:
                print(f"File type matched: {file_type} for {filename.name}")
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
                    if verbose:
                        print(
                            f"Created folder: {folder_date_path.relative_to(base_path)}"
                        )
                except FileExistsError:
                    pass
                if verbose:
                    print(
                        f"Moving {filename.name} to {folder_date_path.relative_to(base_path)}"
                    )
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
                if verbose:
                    print(f"Created folder: {other_date_path.relative_to(base_path)}")
            except FileExistsError:
                pass
            if verbose:
                print(
                    f"Moving {filename.name} to {other_date_path.relative_to(base_path)}"
                )
            shutil.move(filename, other_date_path.joinpath(filename.name))
