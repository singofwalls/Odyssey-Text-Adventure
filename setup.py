import sys

from cx_Freeze import setup, Executable


build_exe_options = {"include": "pygame"}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="The Odyssey",
      version="1.0",
      description="Text Adventure Game",
      options={"build_exe": build_exe_options},
      executables=[Executable("__main__.py", base=base)],
      package_dir={'': ''}, requires=['cx_Freeze', 'pygame', 'jsonpickle']
      )
