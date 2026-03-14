import os
import shutil 
import logging
from config import file_types

logging.basicConfig(
    level = logging.INFO
    format = "%(asctime)s - %(message)s"
    handlers = [
        logging.FileHandler("organzier.log")
        logging.StreamHandler()
    ]
)

def categorize_files(filename):
    name, extension = os.path.splitext(filename)
    extension = extension.lower()
    category = "Miscellaneous"
    for i in file_types:
        if extension in file_types[i]:
            category = i
    return category 

def organize_folder(folder_path):
    for i in os.listdir(folder_path):
        full_path = os.path.join(folder_path, i)
        if os.path.isfile(full_path):
            file_category = categorize_files(i)
            file_destination = os.path.join(folder_path, file_category)
            if not os.path.exists(file_category):
                os.makedirs(file_destination, exist_ok=True)    
            shutil.move(full_path, file_destination)       