from . import tk, ttk

class ARGS_FRAME(ttk.Frame):
    """ 参数框架 """
    def __init__(self, F, choices, callback_FormCommand):
        super().__init__(F)
        self.grid_columnconfigure(0, weight=1)
        
        self.entry_frame = ARGS_ENTRY_FRAME(self, callback_FormCommand)
        self.entry_frame.grid(row=0, column=0, sticky=tk.EW)

        self.choice_frame = ARGS_CHOICES_FRAME(
            self,
            choices,
            callback_FormCommand
        )
        self.choice_frame.grid(row=1, column=0, sticky=tk.EW)

    def get_args(self):
        self.args = []
        return self.args

class ARGS_ENTRY_FRAME(ttk.Frame):
    """ 文本框参数指定 """
    def __init__(self, F, callback_FormCommand):
        super().__init__(F)
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self, text="选择输出路径:（默认为./output）").grid(  # 自定义输出路径
            row=0, column=0,
            sticky=tk.W,
            padx=(0, 10)
        )
        self.output_filename=tk.Entry(self)
        self.output_filename.grid(
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
    def __init__(self, F, choices, callback_FormCommand): # choices:{choice:tk.BooleanVar()}
        super().__init__(F)
        self.grid_columnconfigure(1, weight=1)

        self.choices = choices
        self.args = {}

        for index, (choice, var) in enumerate(self.choices.items()):
            tk.Checkbutton(
                self,
                text=choice,
                variable=var,
                command=1 # lambda: self.args.update({index:choice}) if var.get() else del self.args[index]
            ).grid(
                row=0, column=index,
                sticky=tk.W,
                padx=(0,10)
            )
