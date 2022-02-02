import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    filelist = os.listdir(dirname)
    
    for file in filelist:
        if os.stat(file) >= size_in_kb:
            yield file
    pass