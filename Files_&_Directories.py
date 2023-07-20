from pathlib import Path

# Absolute path
#C:\Program Files\Microsoft
# Relative path

path = Path("ecommerce")
print(path.exists())

This is used to make a directory
path2 = Path("emails")
print(path2.mkdir())


This is used to reemove a directory
path2 = Path("emails")
print(path2.rmdir())


# This used to search through the current path of the directory so other files in the directory like Python files and other things
path = Path()
for file in path.glob("*.py"):
    print(file)