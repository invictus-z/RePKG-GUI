import tkinter as tk
from tkinter import ttk

from Page import SINGLE_EXTRACTOR, MULTI_EXTRACTOR

if __name__=="__main__":
    root = tk.Tk()
    root.title("RePKG-GUI")
    root.geometry("800x600")

    # 创建选项卡容器
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    #1# PKG EXTRACTOR
    extractor = ttk.Notebook(notebook)
    extractor.pack(fill=tk.BOTH, expand=True)
    notebook.add(extractor, text="提取")

    single_extractor_frame = SINGLE_EXTRACTOR(extractor)
    multi_extractor_frame = MULTI_EXTRACTOR(extractor)

    # 检测rePKG是否存在 & repkg info --version
    # 多态调用rePKG.exe

    #2# PKG/TEX CONVERTOR
    convertor = ttk.Notebook(notebook)
    convertor.pack(fill=tk.BOTH, expand=True)
    notebook.add(convertor, text="转换")

    #3# PKG/TEX INFO
    info = ttk.Frame(notebook)
    info.pack(fill=tk.BOTH, expand=True)
    notebook.add(info, text="信息")

    #3# PKG/TEX INFO
    help = ttk.Frame(notebook)
    help.pack(fill=tk.BOTH, expand=True)
    notebook.add(help, text="帮助")

    #3# PKG/TEX INFO
    contact = ttk.Frame(notebook)
    contact.pack(fill=tk.BOTH, expand=True)
    notebook.add(contact, text="联系作者")

    root.mainloop()