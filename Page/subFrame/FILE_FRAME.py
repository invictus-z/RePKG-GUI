from . import tk, ttk

class FILE_FRAME(ttk.Frame):
    """ 文件选取框架 """
    def __init__(self, F, callback_ChangeLabel, callback_FormCommand):
        super().__init__(F)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.callback_ChangeLabel = callback_ChangeLabel
        self.callback_FormCommand = callback_FormCommand

        self.label = tk.Label(self)
        self.label.grid(      ### 计划完成拖动处理
            row=0, column=0,
            sticky=tk.W,
            padx=(0, 10)
        )
        self.input_filename = tk.Entry(self) ### 拖动处理
        self.input_filename.grid(
            row=0, column=1,
            sticky=tk.EW,
            padx=(0, 10)
        )
        tk.Button(self, text="选择", command=self.check_input_filename).grid(
            row=0, column=2,
            sticky=tk.E
        )
    
    def check_input_filename(self):
        if self.input_filename:
            # check input
            self.callback_ChangeLabel(f"你选择了{self.input_filename}")
            self.callback_FormCommand("input_filename", self.input_filename.get())