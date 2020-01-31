import zipfile

with zipfile.ZipFile('files.zip', 'r') as my_zip:
    print(my_zip.namelist())
    my_zip.extractall("files_folder")
    # specific file
    my_zip.extract('tree.png')
    print("done...")