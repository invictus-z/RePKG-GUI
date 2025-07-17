import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def input_check():
    if 1:
        result_label.config(text="你选择了PKG文件")
    return 0
def input_check2():
    return 0

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

#1#1# 标签页 1-1：单个提取
single_extractor = ttk.Frame(extractor)
single_extractor.grid_columnconfigure(0, weight=1)
extractor.add(single_extractor, text="Single Extract")

#1#1# 输入框架
input_file_frame = tk.Frame(single_extractor)
input_file_frame.grid(row=0, column=0, sticky="ew")

input_file_frame.grid_columnconfigure(1, weight=1)
input_file_frame.grid_rowconfigure(0, weight=1)

tk.Label(input_file_frame, text="选择PKG文件:").grid(
    row=0, column=0,
    sticky=tk.W,
    padx=(0, 10)
)
tk.Entry(input_file_frame).grid(
    row=0, column=1,
    sticky=tk.EW,
    padx=(0, 10)
)
tk.Button(input_file_frame, text="选择", command=input_check).grid(
    row=0, column=2,
    sticky=tk.E
)

#1#1# 参数框架
input_args_frame = tk.Frame(single_extractor)
input_args_frame.grid(row=1, column=0, sticky="ew")
input_args_frame.grid_columnconfigure(0, weight=1)

input_args_entry_frame = tk.Frame(input_args_frame)
input_args_entry_frame.grid(row=0, column=0, sticky="ew")
input_args_entry_frame.grid_columnconfigure(1, weight=1)
tk.Label(input_args_entry_frame, text="选择输出路径:（默认为./output）").grid( #  自定义输出路径
    row=0, column=0,
    sticky=tk.W,
    padx=(0, 10)
)
tk.Entry(input_args_entry_frame).grid(
    row=0, column=1,
    sticky=tk.EW,
    padx=(0, 10)
)
tk.Button(input_args_entry_frame, text="选择", command=input_check2()).grid(
    row=0, column=2,
    sticky=tk.E
)

input_args_choice_frame = tk.Frame(input_args_frame)
input_args_choice_frame.grid(row=1, column=0, sticky="ew")
input_args_choice_frame.grid_columnconfigure(1, weight=1)

tk.Checkbutton(
    input_args_choice_frame,
    text="仅输出图像",
    variable=tk.BooleanVar(),
    command=lambda: print("仅输出图像选项被选中")
).grid(
    row=0, column=0,
    sticky=tk.W,
    padx=(0,10)
)
tk.Checkbutton(
    input_args_choice_frame,
    text="XX",
    variable=tk.BooleanVar(),
    command=lambda: print("XX选项被选中")
).grid(
    row=0, column=1,
    sticky=tk.W,
    padx=(0,10)
)

# 确定按钮
choice_frame = tk.Frame(single_extractor)
choice_frame.grid(row=2, column=0)
choice_frame.grid_columnconfigure(0, weight=1)

result_label = tk.Label(choice_frame, text="你还未选择pkg文件")
result_label.grid(
    row=0, column=0, 
    sticky=tk.W,
    padx=(10, 0)
)
tk.Button(choice_frame, text="确定").grid(
    row=0, column=1, 
    sticky=tk.E
)

# 输出框架
output_frame = tk.Frame(single_extractor)
output_frame.grid(row=3, column=0, sticky="ew")

tk.Label(output_frame, text="输出结果:").pack(side=tk.TOP, padx=10, pady=5)
# 图片预览显示
image = ImageTk.PhotoImage(Image.open("test.png").resize((800,400)))
label = tk.Label(output_frame, image=image)
label.image = image  # 保持对图片的引用，避免被垃圾回收
label.pack(padx=10, pady=10)

# 标签页 1-2：多个提取
extract_multiple = ttk.Frame(extractor)
extractor.add(extract_multiple, text="Multiple Extract")



root.mainloop()