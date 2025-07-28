from . import tk, ttk

class ARGS_FRAME(ttk.Frame):
    """ 参数框架 """
    def __init__(self, F):
        super().__init__(F)
        self.grid_columnconfigure(0, weight=1)
        
        self.entry_frame = ARGS_ENTRY_FRAME(self)
        self.entry_frame.grid(row=0, column=0, sticky=tk.EW)

        self.choice_frame = ARGS_CHOICES_FRAME(
            self,
            {
                "仅保留图像":tk.BooleanVar()
            }
        )
        self.choice_frame.grid(row=1, column=0, sticky=tk.EW)

    def get_args(self):
        self.args = []
        return self.args

class ARGS_ENTRY_FRAME(ttk.Frame):
    """ 文本框指定参数 """
    def __init__(self, F):
        super().__init__(F)
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self, text="选择输出路径:（默认为./output）").grid(  # 自定义输出路径
            row=0, column=0,
            sticky=tk.W,
            padx=(0, 10)
        )
        tk.Entry(self).grid(
            row=0, column=1,
            sticky=tk.EW,
            padx=(0, 10)
        )
        tk.Button(self, text="选择", command=self.check_input).grid(
            row=0, column=2,
            sticky=tk.E
        )
    def check_input():
        pass

class ARGS_CHOICES_FRAME(ttk.Frame):
    """ 复选框指定参数 """
    def __init__(self, F, choices): # choices:{choice:tk.BooleanVar()}
        super().__init__(F)
        self.grid_columnconfigure(1, weight=1)

        self.choices = choices

        for index, (choice, var) in enumerate(self.choices.items()):
            tk.Checkbutton(
                self,
                text=choice,
                variable=var,
                command=lambda: print(f"{choice}选项被选中") if var.get() else print(f"{choice}选项被取消")
            ).grid(
                row=0, column=index,
                sticky=tk.W,
                padx=(0,10)
            )
        