# 📂 File Organizer Utility

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
- **Modules:** `os`, `shutil`, `datetime`, `argparse`, `mimetypes`

## 📦 Installation

### File Structure

```bash
file-organizer/
├── file_organizer.py          # Main script
├── test_file_organizer.py     # Unit tests
├── file_types_config.py       # Optional: file type mappings
├── README.md                  # Documentation
├── .gitignore                 # Git config
└── examples/                  # Sample inputs or config (optional)
```

### Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/file-organizer.git
cd file-organizer
```

Install dependencies (only standard libraries used; no installation required).

## 🧪 Usage

Basic usage:

```bash
python3 file_organizer.py --path /path/to/target/directory
```

### Optional arguments

| Flag          | Description                             |
| ------------- | --------------------------------------- |
| `--path`      | Path to the target directory (required) |
| `--by-date`   | Organize by creation/modification date  |
| `--dry-run`   | Preview actions without moving files    |
| `--recursive` | Scan subdirectories recursively         |
| `--verbose`   | Print details of every file action      |

### Example

```bash
python file_organizer.py --path ~/Downloads --by-date --verbose
```

## 📂 Folder Mapping Logic

By default, files are sorted by extension into these categories:

```python
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".md"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".sh", ".bat"],
    "Others": []
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
