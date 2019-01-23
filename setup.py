import cx_Freeze
import sys
import os
import matplotlib

os.environ["TCL_LIBRARY"] = "C:\\LOCAL_TO_PYTHON\\PYTHON35-32\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"]  = "C:\\LOCAL_TO_PYTHON\\PYTHON35-32\\tcl\\tk8.6"

bse = None

if sys.platform=="win32":
    base = "win32GUI"

executables = [cx_Freeze.Executable("noni.py", base=None,
                                    icon = r"noni.ico",
                                    shortcutName = "Noni",
                                    shortcutDir = "DesktopFolder"
                                    )]

cx_Freeze.setup(
    name = "Noni",
    options = {"build_exe":{"packages":{"numpy"}}},
    version = "0.1",
    description = "HELLO I AM A CHATBOT CALLED NONI VERSION 0.1",
    executables = executables
    )
