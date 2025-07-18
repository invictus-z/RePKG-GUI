from . import tk, ttk

class FILE_FRAME():
    """ 文件选取框架 """
    def __init__(self, F, callback_change_label):
        self.frame = ttk.Frame(F)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.callback_change_label = callback_change_label

        self.label = tk.Label(self.frame)
        self.label.grid(      # 计划完成拖动处理
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