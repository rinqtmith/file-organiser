import os

from pathlib import Path

# use hard coded path for testing purposes
PATH = Path("/Users/fatihavci/dev/boot-dev/portfolio/example_folder")


def main():
    # get files and directories in the current directory
    folders = []
    files = []
    for filename in os.listdir(PATH):
        # print folders and files separately
        if os.path.isdir(os.path.join(PATH, filename)):
            folders.append(filename)
        if os.path.isfile(os.path.join(PATH, filename)):
            files.append(filename)
        # separate files according to their extensions
    print(f"Folders: {folders}")
    print(f"Files: {files}")


if __name__ == "__main__":
    main()
