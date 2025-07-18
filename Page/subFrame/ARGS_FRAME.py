from . import tk, ttk

class ARGS_FRAME():
    """ 参数框架 """
    def __init__(self, F):
        self.frame = ttk.Frame(F)
        self.frame.grid_columnconfigure(0, weight=1)
        
        self.entry_frame = ARGS_ENTRY_FRAME(self.frame)
        self.entry_frame.frame.grid(row=0, column=0, sticky=tk.EW)

        self.choice_frame = ARGS_CHOICES_FRAME(
            self.frame,
            {
                "仅保留图像":tk.BooleanVar()
            }
        )
        self.choice_frame.frame.grid(row=1, column=0, sticky=tk.EW)

    def get_args(self):
        self.args = []
        return self.args

class ARGS_ENTRY_FRAME():
    """ 文本框指定参数 """
    def __init__(self, F):
        self.frame = ttk.Frame(F)
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

class ARGS_CHOICES_FRAME():
    """ 复选框指定参数 """
    def __init__(self, F, choices): # choices={choice:tk.BooleanVar()}
        self.frame = ttk.Frame(F)
        self.frame.grid_columnconfigure(1, weight=1)

        self.choices = choices

        for index, (choice, var) in enumerate(self.choices.items()):
            tk.Checkbutton(
                self.frame,
                text=choice,
                variable=var,
                command=lambda: print(f"{choice}选项被选中") if var.get() else print(f"{choice}选项被取消")
            ).grid(
                row=0, column=index,
                sticky=tk.W,
                padx=(0,10)
            )
        