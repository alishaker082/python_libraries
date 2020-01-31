import zipfile 

my_zip = zipfile.ZipFile('files.zip', 'w')
my_zip.write('tree.dot')
my_zip.write('tree1.dot')
my_zip.write('tree.png')

my_zip.close()
print("done....")

# Second Way
with zipfile.ZipFile('files1.zip', 'w') as my_zip:
    my_zip.write('tree.dot')
    my_zip.write('tree1.dot')
    my_zip.write('tree.png')
    print("done....")

# Second Way with compresion
with zipfile.ZipFile('files2.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('tree.dot')
    my_zip.write('tree1.dot')
    my_zip.write('tree.png')
    print("done....")