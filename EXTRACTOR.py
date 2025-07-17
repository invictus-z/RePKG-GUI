import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

''' structure
extractor
- input_frame
    - file_frame
    - args_frame
- output_frame
'''

class EXTRACTOR():
    def __init__(self, N):
        self.frame = ttk.frame(N)
        self.frame.grid_columnconfigure(0, weight=1)

        self.input_frame = INPUT_FRAME(self.frame, self.extractor_exec)
        self.output_frame = OUTPUT_FRAME(self.frame)


    def extractor_exec(self): # 回调执行
        # 维护一个参数列表 self.input_frame.
        try:
            # example
            result = subprocess.run(
                ["ls", "-l"],
                capture_output=True,
                text=True,   
                check=True      
            )
            print("命令输出：")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"命令执行失败：{e.stderr}")
        except FileNotFoundError:
            print("错误：找不到该命令")
        except Exception as e:
            print(f"发生未知错误：{e}")
        

class INPUT_FRAME():
    """ 输入框架 """
    def __init__(self, F, callback_exec=None):
        self.frame = ttk.frame(F)
        self.frame.grid_columnconfigure(0, weight=1)
        self.callback_exec = callback_exec

        self.file_frame = FILE_FRAME(self.frame, self.change_result_label)
        self.args_frame = ARGS_FRAME(self.frame)

        self.result_label = tk.Label(self.frame, text="你还未选择pkg文件")
        self.result_label.grid(
            row=2, column=0, 
            sticky=tk.W,
            padx=(10, 0)
        )
        tk.Button(self.frame, text="确定", command=self.on_button_click).grid(
            row=2, column=1, 
            sticky=tk.E
        )

    def on_button_click(self):
        self.callback_exec()

    def change_result_label(self, text):
        self.result_label.config(text=text)

class FILE_FRAME():
    """ 文件选取框架 """
    def __init__(self, F, callback_change_label):
        self.frame = ttk.frame(F)
        self.frame.grid(row=0, column=0, sticky="ew")
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.callback_change_label = callback_change_label

        self.label = tk.Label(self.frame)
        self.label.grid(
            row=0, column=0,
            sticky=tk.W,
            padx=(0, 10)
        )
        self.filename = tk.Entry(self.frame) ######
        self.filename.grid(
            row=0, column=1,
            sticky=tk.EW,
            padx=(0, 10)
        )
        tk.Button(self.frame, text="选择", command=self.check_input_filename).grid(
            row=0, column=2,
            sticky=tk.E
        )
    def check_input_filename(self):
        # check input
        self.callback_change_label(f"你选择了{self.filename}")



class ARGS_FRAME():
    """ 参数框架 """
    def __init__(self, F):
        self.frame = ttk.frame(F)
        self.frame.grid(row=1, column=0, sticky="ew")
        self.frame.grid_columnconfigure(0, weight=1)
        
        self.entry_frame = INPUT_ARGS_ENTRY_FRAME(self.frame)
        self.choice_frame = INPUT_ARGS_CHOICE_FRAME(self.frame)
    def get_args(self):
        self.args = []
        return self.args

class INPUT_ARGS_ENTRY_FRAME():
    """ 文本框指定参数 """
    def __init__(self, F):
        self.frame = ttk.frame(F)
        self.frame.grid(row=0, column=0, sticky="ew")
        self.frame.grid_columnconfigure(1, weight=1)

        tk.Label(self.frame, text="选择输出路径:（默认为./output）").grid(  # 自定义输出路径
            row=0, column=0,
            sticky=tk.W,
            padx=(0, 10)
        )
        tk.Entry(self.frame).grid(
            row=0, column=1,
            sticky=tk.EW,
            padx=(0, 10)
        )
        tk.Button(self.frame, text="选择", command=self.check_input).grid(
            row=0, column=2,
            sticky=tk.E
        )
    def check_input():
        pass

class INPUT_ARGS_CHOICE_FRAME():
    """ 复选框指定参数 """
    def __init__(self, F):
        self.frame = ttk.frame(F)
        self.frame.grid(row=1, column=0, sticky="ew")
        self.frame.grid_columnconfigure(1, weight=1)

        option1_var = tk.BooleanVar()
        tk.Checkbutton(
            self.frame,
            text="仅输出图像",
            variable=option1_var,
            command=lambda: print("仅输出图像选项被选中")
        ).grid(
            row=0, column=0,
            sticky=tk.W,
            padx=(0,10)
        )
        option2_var = tk.BooleanVar()
        tk.Checkbutton(
            self.frame,
            text="XX",
            variable=option2_var,
            command=lambda: print("XX选项被选中")
        ).grid(
            row=0, column=1,
            sticky=tk.W,
            padx=(0,10)
        )

# 输出框架
class OUTPUT_FRAME():
    def __init__(self, F):
        self.frame = ttk.frame(F)
        self.frame.grid(row=3, column=0, sticky="ew")

    def show_image(self):
        tk.Label(self.frame, text="输出结果:").pack(side=tk.TOP, padx=10, pady=5)
        # 图片预览显示
        image = ImageTk.PhotoImage(Image.open("test.png").resize((800,400)))
        label = tk.Label(self.frame, image=image)
        label.image = image  # 保持对图片的引用，避免被垃圾回收
        label.pack(padx=10, pady=10)


# 继承EXTRACTOR的两个子类构建选项卡的两部分
class SINGLE_EXTRACTOR(EXTRACTOR):
    def __init__(self, extractor):
        super().__init__(extractor)
        self.input_label.config(text="选择PKG文件:")
        extractor.add(self, text="Single Extract")

class MULTI_EXTRACTOR(EXTRACTOR):
    pass