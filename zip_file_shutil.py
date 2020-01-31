import shutil

shutil.make_archive('another', 'zip', 'files_folder')

shutil.unpack_archive('another.zip', 'another')