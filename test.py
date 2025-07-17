import tkinter as tk
from tkinter import ttk

def show_selections():
    selected_options = [option for option, var in options.items() if var.get()]
    result_label.config(text=f"你选择了: {', '.join(selected_options)}")

root = tk.Tk()
root.title("框架内的复选框示例")
root.geometry("400x300")

# 创建一个框架
frame = ttk.LabelFrame(root, text="请选择你喜欢的水果", padding="10")
frame.pack(fill="both", expand=True, padx=10, pady=10)

# 定义复选框选项
options = {
    "苹果": tk.BooleanVar(),
    "香蕉": tk.BooleanVar(),
    "橙子": tk.BooleanVar(),
    "草莓": tk.BooleanVar()
}

# 在框架内创建复选框
for option, var in options.items():
    ttk.Checkbutton(
        frame,
        text=option,
        variable=var,
        command=show_selections
    ).pack(anchor="w", pady=5)

# 显示结果的标签
result_label = ttk.Label(root, text="你还没有选择任何水果", padding="10")
result_label.pack(fill="x")

root.mainloop()