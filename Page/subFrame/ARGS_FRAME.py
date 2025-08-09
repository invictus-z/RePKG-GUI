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

class ARGS_ENTRY_FRAME(ttk.Frame):
    """ 文本框指定参数 """
    def __init__(self, F, callback_FormCommand):
        super().__init__(F)
        self.grid_columnconfigure(1, weight=1)
        self.callback_FormCommand=callback_FormCommand

        tk.Label(self, text="选择输出路径:（默认为./output）").grid(  # 自定义输出路径
            row=0, column=0,
            sticky=tk.W,
            padx=(0, 10)
        )
        self.output_folder=tk.Entry(self)
        self.output_folder.grid(
            row=0, column=1,
            sticky=tk.EW,
            padx=(0, 10)
        )
        tk.Button(self, text="选择", command=self.check_output_folder).grid(
            row=0, column=2,
            sticky=tk.E
        )
    
    def check_output_folder(self):
        # check
        self.callback_FormCommand("output_folder", self.output_folder.get())

class ARGS_CHOICES_FRAME(ttk.Frame):
    """ 复选框指定参数 """
    def __init__(self, F, choices, callback_FormCommand): # choices:[[choice,arg,tk.BooleanVar()]]
        super().__init__(F)
        self.grid_columnconfigure(1, weight=1)

        for index, choice in enumerate(choices):
            tk.Checkbutton(
                self,
                text=choice[0],
                variable=choice[2],
                command=lambda: callback_FormCommand("choices")
            ).grid(
                row=index//2, column=index%2,
                sticky=tk.W,
                padx=(0,10)
            )
