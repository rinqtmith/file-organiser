# 📂 File Organiser Utility

A command-line Python script that automatically organizes files in a given directory
by file type, creation date, or custom logic. This tool helps de-clutter downloads
folders, desktop directories, or any workspace by categorizing and moving files into
structured subfolders.

## 🚀 Features

- 🔍 Scan a target directory (recursively or non-recursively)
- 📁 Automatically create subfolders by:

  - File extension (e.g., `.pdf`, `.jpg`)
  - File type category (e.g., Images, Documents, Archives)
  - Creation or modification date (e.g., `2025-05`)

- 🔄 Optional dry-run mode to simulate the organization
- 🧠 Configurable mapping of file types to folders
- 🛉 Ignores system or hidden files

## 🛠️ Tech Stack

- **Language:** Python 3
- **Modules:** `os`, `shutil`, `datetime`, `argparse`

## 📦 Installation

### File Structure

```bash
file-organiser/
├── src/
│   ├── arg_parser.py             # CLI argument parsing
│   ├── check_files.py            # Validates file conditions
│   ├── handle_path.py            # Resolves and sanitizes paths
│   ├── move_file_to_folder.py    # Moves files into categorized folders
│   ├── remove_empty_folders.py   # Deletes empty directories
├── file_types_config.py          # File extension-category mapping
├── main.py                       # Entry point of the program
├── README.md
├── LICENSE
└── .gitignore
```

### Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/file-organiser.git
cd file-organiser
```

Install dependencies (only standard libraries used; no installation required).

## 🧪 Usage

Basic usage:

```bash
python3 main.py [-h] [--dry-run] [-b] [-r] [-a] [-v] path
```

### Positional arguments

| Argument | Description                             |
| -------- | --------------------------------------- |
| `path`   | Path to the directory to organize files |

### Optional arguments

| Flag                    | Description                                |
| ----------------------- | ------------------------------------------ |
| `-h`, `--help`          | Show this help message and exit            |
| `--dry-run`             | Perform a dry run without making changes   |
| `-b`, `--by-date`       | Organize files by modification date        |
| `-r`, `--recursive`     | Organize files recursively                 |
| `-a`, `--recursive-all` | Organize all files recursively (max depth) |
| `-v`, `--verbose`       | Enable verbose output for logging          |

### Example

```bash
python main.py ~/Downloads --by-date --verbose
```

## 📂 Folder Mapping Logic

By default, files are sorted by extension into these categories:

```python
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".md"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Videos": [".mp4", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Executables": [".exe", ".sh", ".bat"],
}
```

You can modify this mapping in the script to suit your needs.

## 📈 Potential Improvements

- GUI support with Tkinter
- Configuration file for user-defined rules
- Logging to a file
- Scheduling support via cron or Task Scheduler

## 📄 License

MIT License

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

Disclaimer
_(Generated with the help of AI.)_
