# Automatic File Organizer

A Python script that automatically organizes files in any folder into categorized subfolders based on file extension. Supports undo to restore all files back to their original location.

---

## Features

- Scans any folder and categorizes files by extension
- Moves files into labeled subfolders automatically
- Supports undo — restores all files back to the root folder
- Logs every action to the terminal and to a .log file
- Handles 40+ file extensions across 11 categories
- Defensive input handling for invalid or malformed paths

---

## Project Structure
```
file-organizer/
├── organizer.py       # Main script — organizes and undoes
├── config.py          # File type categories and extensions
├── organizer.log      # Auto-generated log file after first run
├── TDD.md             # Technical Design Document
└── README.md          # Project documentation
```

---

## How to Run

### 1. Clone the repository
```
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

### 2. Run the script
```
python organizer.py
```

### 3. Follow the prompts
```
Enter folder path: C:\Users\YourName\Downloads
Type 'organize' or 'undo': organize
```

---

## Undo / Restore

If you want to reverse the organization and move all files back to the original folder, run the script and choose undo at the prompt:
```
Enter folder path: C:\Users\YourName\Downloads
Type 'organize' or 'undo': undo
```

The script will move every file from the category subfolders back to the root folder and remove the now-empty subfolders.

Note: if two files from different categories share the same filename, one may overwrite the other during restore. This is an edge case and rarely occurs in practice.

---

## File Categories

| Category | Extensions |
|---|---|
| Text Files | .txt, .rtf, .md |
| Document Files | .doc, .docx, .pdf, .odt |
| Spreadsheet Files | .xls, .xlsx, .csv, .ods |
| Presentation Files | .ppt, .pptx, .odp |
| Image Files | .jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg |
| Audio Files | .mp3, .wav, .aac, .flac, .ogg |
| Video Files | .mp4, .avi, .mov, .mkv, .wmv |
| Programming Files | .py, .c, .cpp, .java, .js, .html, .css |
| Archive Files | .zip, .rar, .7z, .tar, .gz |
| Database Files | .sql, .db, .sqlite, .mdb |
| Executable Files | .exe, .bat, .sh |
| Miscellaneous | Everything else |

---

## Sample Log Output
```
2025-01-14 10:23:01 - Moved: resume.pdf to Document Files
2025-01-14 10:23:01 - Moved: photo.jpg to Image Files
2025-01-14 10:23:01 - Moved: project.zip to Archive Files
2025-01-14 10:23:01 - Skipped: Image Files (not a file)
2025-01-14 10:23:01 - Restored: resume.pdf to Document Files
2025-01-14 10:23:01 - Removed folder: Document Files
```

---

## Requirements

- Python 3.x
- No external libraries — uses only built-in modules (os, shutil, logging)

---

## Customization

To add new file categories or extensions, edit config.py:
```python
file_types = {
    "3D Files": [".obj", ".stl", ".fbx"],
    # add more categories here
}
```

---

## Author

Built by Shruti Vasudev Jahagirdar.