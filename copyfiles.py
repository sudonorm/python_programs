# python 3 and above needed

import os, shutil

def copy_files(srcdir=r"", dstdir=r"", extens="", operation="copy"):
    """ This function moves/copies files from one folder to another, based on the selected operation.
        args:
            srcdir: source directory where the files to be moved/copied are located
            dstdir: destination directory, where the files are to be moved/copied
            extens: file extension e.g. ".py"
            operation: "move" to move files completely or "copy" to copy files

        Note: when passing in the directories, the paths should be prefixed with a "r" to avoid truncation errors
        If the file already exists in the destination directory, use copy to overwrite
    """

    source = os.listdir(srcdir)

    dstdir = str(dstdir)
    
    extens = str(extens)
    
    if not extens[0] == ".":
        extens = "."+extens
    
    source = [x for x in source]
    
    for files in source:
        if files.endswith(extens):
            pathname = os.path.join(srcdir, files)
            if os.path.isfile(pathname):
                if operation == "move":
                    shutil.move(pathname, dstdir)
                elif operation == "copy":
                    shutil.copy2(pathname, dstdir)