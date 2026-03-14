import os
import shutil 
import logging
from config import file_types

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(message)s",
    handlers = [
        logging.FileHandler("organizer.log"),
        logging.StreamHandler()
    ]
)

def categorize_files(filename):
    # Returns category folder name of particular filename.
    name, extension = os.path.splitext(filename)
    extension = extension.lower()
    category = "Miscellaneous"
    for i in file_types:
        if extension in file_types[i]:
            category = i
    return category 

def organize_folder(folder_path):
    # Scans folder and organizes them into sub-folders based on file type categories.
    for i in os.listdir(folder_path):
        full_path = os.path.join(folder_path, i)
        if os.path.isfile(full_path):
            file_category = categorize_files(i)
            file_destination = os.path.join(folder_path, file_category)
            if not os.path.exists(file_category):
                os.makedirs(file_destination, exist_ok=True)    
            shutil.move(full_path, file_destination)  
            logging.info(f"Moved: {i} to {file_category}")
        else:
            logging.warning(f"Skipped: {i} (not a file)")     
    
def undo_organize(folder_path):
    """Moves all files back to the root folder from category subfolders."""
    for category in os.listdir(folder_path):
        category_path = os.path.join(folder_path, category)
        if os.path.isdir(category_path):                          # only look inside folders
            for file in os.listdir(category_path):
                full_path = os.path.join(category_path, file)
                if os.path.isfile(full_path):
                    shutil.move(full_path, folder_path)           # move back to root
                    logging.info(f"Restored: {file} to {category}")
            os.rmdir(category_path)                               # remove empty folder
            logging.info(f"Removed folder: {category}")

if __name__ == "__main__":
    path = input("Enter folder path: ").strip('"')  # ← removes accidental quotes
    action = input("Type 'organize' or 'undo': ")
    if action == "organize":
        organize_folder(path)
    elif action == "undo":
        undo_organize(path)
    else:
        print("Invalid action. Please type 'organize' or 'undo'.")