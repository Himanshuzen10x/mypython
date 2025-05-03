import os

print("Current Directory:", os.getcwd())
# print(os.listdir())

# Create new folder
try:
    os.mkdir("test_folder")
    print("Folder created.")
except Exception as e :
    print("error")

# os.rename("test_folder", "renamed_folder")
# print("Folder renamed.")

# os.remove("test_folder")
# print("File deleted.")

for file in os.listdir():
    if file.endswith(".txt"):
        print("text file :" , file)