import os

print("Current Folder:", os.getcwd())

print("Dataset Exists:", os.path.exists("dataset"))

if os.path.exists("dataset"):
    print("Folders:", os.listdir("dataset"))