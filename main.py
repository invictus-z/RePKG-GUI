import tkinter as tk
from tkinter import ttk
from EXTRACTOR import SINGLE_EXTRACTOR, MULTI_EXTRACTOR

root = tk.Tk()
root.title("RePKG-GUI")
root.geometry("800x600")

# 创建选项卡容器
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

#1# 标签页 1：PKG EXTRACTOR
extractor = ttk.Notebook(notebook)
extractor.pack(fill=tk.BOTH, expand=True)
notebook.add(extractor, text="Extractor")

extractor_frame = SINGLE_EXTRACTOR(extractor)

# 多态调用rePKG.exe

#2# 标签页 2：PKG CONVERTOR

root.mainloop()