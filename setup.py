import os,sys
from cx_Freeze import setup, Executable

packages = [
    "Page",
    "Page.subFrame"
]

includes = [
]

excludes = [
    "temp"
]

include_files = [
]

'''
if sys.platform == "win32":
    # 添加 tkinter 运行时文件
    try:
        import tkinter
        tcl_dir = os.path.dirname(tkinter.__file__)
        include_files.extend([
            (os.path.join(tcl_dir, "tcl8.6"), "tcl"),
            (os.path.join(tcl_dir, "tk8.6"), "tk")
        ])
    except ImportError:
        pass
'''

build_exe_options = {
    "packages": packages,
    "includes": includes,
    "excludes": excludes,
    "include_files": include_files,
    "zip_include_packages": "*",  # 把大部分库打包进 zip 减小体积
    "zip_exclude_packages": [],
    "optimize": 2,
    "build_exe": "build/RePKG-GUI-Windows",
}


executables = [
    Executable(
        script = "main.py",
        base = "Win32GUI" if sys.platform == "win32" else None,
        target_name = "repkg_gui.exe" if sys.platform == "win32" else "repkg_gui",
        # icon="app_icon.ico"
    )
]

setup(
    name="RePKG-GUI",
    version="0.1.0a0",
    description="none",
    options={"build_exe": build_exe_options},
    executables=executables
)