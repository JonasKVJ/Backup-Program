#! python3
# f-strings are only compatible with Python >= 3.6
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os
import shutil
import zipfile
from pathlib import Path

# Back up the entire contents of "folder" into a ZIP file.


def backupToZip(folder):

    folder = os.path.abspath(folder)   # make sure folder is absolute

    # Delete old zipfile, because only one backup is needed at a time
    zipFilename = os.path.basename(folder) + '.zip'
    if os.path.exists(zipFilename):
        os.unlink(f'{os.getcwd()}/{zipFilename}')
        print(f'Deleted old {folder}/{zipFilename}')

    # TODO: Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            if filename.endswith('.zip'):
                continue   # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


# Windows Format: backupToZip('C:\\delicious')
my_folder_1 = Path.home()/'Insert/Your/Folder/Path/Here'
backupToZip(my_folder_1)

my_folder_2 = Path.home()/'Insert/Another/Folder/Path/Here'
backupToZip(my_folder_2)

my_folder_3 = Path.home()/'Insert/Another/Folder/Path/Here'
backupToZip(my_folder_3)
