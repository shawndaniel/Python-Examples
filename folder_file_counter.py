__author__ = 'Shawn Daniel'
"""
Initially decided to write this for some server software although, it is a good example
for python beginners and can be generally useful with more capabilities added.
"""

import anydbm
import os
from sys import argv
import time


path = "C:\\test"
# script, path = argv
folders = {key: 0 for key in os.listdir(path) if os.path.isdir(os.path.join(path, key))}

# create a storage file for purposes of tracking future changes to file count
tracker = anydbm.open('tracker', 'c')


def calc_age(folder_date):
    """Calculates age by subtracting the date of folder creation with the current local date then formats result"""
    current_date = time.localtime()
    month = current_date[1] - folder_date[1]
    day = current_date[2] - folder_date[2]
    year = current_date[0] - folder_date[0]
    while month < 0 or day < 0 or year < 0:
        if year < 0:
            year += 1
            month -= 12
        elif month < 0:
            year -= 1
            month += 12
        elif day < 0:
            month -= 1
            day += 30
    return month, day, year


def count_files():
    """prints the number of files within each directory"""
    for folder in folders.keys():
        folder_date = time.localtime(os.stat(os.path.join(path, folder)).st_ctime)
        month, day, year = calc_age(folder_date)
        file_count = len(os.listdir(os.path.join(path, folder)))
        if folder in tracker.keys():
            new_changes = file_count - tracker[folder][0]
        else:
            new_changes = file_count
        duration_formatted = "%d Years, %d Months, %d days" % (year, month, day)
        tracker[folder] = file_count, new_changes, duration_formatted

    # sort the items in 'folders' dict by file count in descending order
    sorted_count = sorted(tracker.iteritems(), key=lambda x: x[1], reverse=True)
    # format and print the dictionary values
    for x, y in sorted_count:
        if y[0] > 0:
            output = "{:<35} {:^10} {} {:>15} {} {:>10} {}".format(
                x, 'File Count:', y[0], 'New Count:', y[1], 'Age:', y[2])
            print output
        else:
            pass
    tracker.close()

count_files()
