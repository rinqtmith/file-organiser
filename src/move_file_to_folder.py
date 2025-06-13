import os
import shutil

from datetime import datetime

from file_types_config import FILE_TYPES


def move_file_to_folder(
    base_path, filename, file_path, dry_run, by_date, r_all, verbose
):
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
