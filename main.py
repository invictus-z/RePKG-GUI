import tkinter as tk
from tkinter import ttk

from Page import SINGLE_EXTRACTOR, MULTI_EXTRACTOR
from Page import CONVERTOR
from Page import INFO
from Page import HELP
from Page import CONTACT

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
    notebook.add(extractor, text="PKG提取")

    single_extractor_frame = SINGLE_EXTRACTOR(extractor)
    multi_extractor_frame = MULTI_EXTRACTOR(extractor)

    #2# PKG/TEX CONVERTOR
    convertor = CONVERTOR(notebook)
    convertor.pack(fill=tk.BOTH, expand=True)
    notebook.add(convertor, text="文件转换")

    #3# PKG/TEX INFO    
    info = INFO(notebook)
    info.pack(fill=tk.BOTH, expand=True)
    notebook.add(info, text="文件信息")

    #4# LOG
    log = ttk.Frame(notebook)
    log.pack(fill=tk.BOTH, expand=True)
    notebook.add(log, text="日志")

    #5# SETTINGS
    settings = ttk.Frame(notebook)
    settings.pack(fill=tk.BOTH, expand=True)
    notebook.add(settings, text="设置") #可选是否执行日志记录（default开启）

    #6# HELP
    help = HELP(notebook)
    help.pack(fill=tk.BOTH, expand=True)
    notebook.add(help, text="帮助/使用说明")  #repkg版本检测

    #7# CONTACT
    contact = CONTACT(notebook, 
        AUTHOR_NAME="invictus", 
        AUTHOR_EMAIL="invictus_star@outlook.com",
        text="开源地址 ：https://github.com/invictus-z/RePKG-GUI"
    )
    contact.pack(fill=tk.BOTH, expand=True)
    notebook.add(contact, text="联系作者")


    # 绑定事件
    update_wrap_length0 = single_extractor_frame.input_frame.update_wrap_length
    update_wrap_length1 = help.update_wrap_length

    root.update_idletasks()

    update_delay = None

    def handle_configure(event):
        global update_delay
        if update_delay:
            root.after_cancel(update_delay)
        # 50ms后执行更新
        update_delay = root.after(50, update_wrap_length0, event)
        update_delay = root.after(50, update_wrap_length1, event)

    root.bind("<Configure>", handle_configure)

    initial_event = type('obj', (object,), {'width': root.winfo_width()})()
    handle_configure(initial_event)

    root.mainloop()