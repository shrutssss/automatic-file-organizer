# Automatic File Organizer

A Python script that automatically organizes files in any folder (e.g. Downloads) into categorized subfolders based on file extension.

---

## Features

- Automatically categorizes files into folders like `Image Files`, `Document Files`, `Video Files`, etc.
- Handles 11 file categories and 40+ file extensions
- Logs every action to the terminal and to `organizer.log`
- Skips subfolders — only processes files
- Puts unrecognized files into a `Miscellaneous` folder

---

## Project Structure

```
file-organizer/
├── organizer.py    # Main script — scans and moves files
├── config.py       # File type categories and extensions
├── organizer.log   # Auto-generated log file after first run
└── README.md       # Project documentation
```

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

### 2. Update the folder path
Open `organizer.py` and change the path at the bottom to your target folder:
```python
if __name__ == "__main__":
    organize_folder(r"C:\Users\YourName\Downloads")  # Windows
    # organize_folder("/home/yourname/Downloads")    # Mac/Linux
```

### 3. Run the script
```bash
python organizer.py
```

---

## 📂 File Categories

| Category | Extensions |
|---|---|
| Text Files | `.txt`, `.rtf`, `.md` |
| Document Files | `.doc`, `.docx`, `.pdf`, `.odt` |
| Spreadsheet Files | `.xls`, `.xlsx`, `.csv`, `.ods` |
| Presentation Files | `.ppt`, `.pptx`, `.odp` |
| Image Files | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg` |
| Audio Files | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg` |
| Video Files | `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv` |
| Programming Files | `.py`, `.c`, `.cpp`, `.java`, `.js`, `.html`, `.css` |
| Archive Files | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Database Files | `.sql`, `.db`, `.sqlite`, `.mdb` |
| Executable Files | `.exe`, `.bat`, `.sh` |
| Miscellaneous | Everything else |

---

## 📋 Sample Log Output

```
2025-01-14 10:23:01 - Moved: resume.pdf → Document Files
2025-01-14 10:23:01 - Moved: photo.jpg → Image Files
2025-01-14 10:23:01 - Moved: project.zip → Archive Files
2025-01-14 10:23:01 - Skipped: Image Files (not a file)
```

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed — uses only built-in modules (`os`, `shutil`, `logging`)

---

## 🔧 Customization

To add new file categories or extensions, simply edit `config.py`:

```python
file_types = {
    "3D Files": [".obj", ".stl", ".fbx"],
    # add more categories here...
}
```

---

## 👨‍💻 Author

Built by Shruti Jahagirdar.