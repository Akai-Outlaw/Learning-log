#Python File Detector 
import os

# file_path = "file/text.txt" #relative path finder
file_path = "/Volumes/Extreme Pro/NEXUS/03 COGNITION/02 Self-Education/Learning-projects/Python/file dection/file" #absoulte path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exist")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("that is a directory")
else:
    print("That location doesn't text")
