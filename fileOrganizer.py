import os
from pathlib import Path

#Dictionary for the suffixes the goes in each directory
SUBDIRECTORIES = {
    "DOCUMENTS" : ['.pdf','.rtf','.txt','.doc','.docx'],
    "AUDIO" : ['.m4a','.m4b','.mp3'],
    "VIDEOS" : ['.mov','.avi','.mp4'],
    "IMAGES" : ['.jpg','.jpeg','.png','heic'],
}


def pickDir(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'OTHERS' # save files that aren't defined in
                    # a new directory named OTHERS 
            
            
def organizeDir():
    for item in os.scandir():
        if item.is_dir(): 
            continue    # don't change the path of the item 
                        # if it's already a directory
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDir(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
        

organizeDir()