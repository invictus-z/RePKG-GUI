from . import tk, ttk, filedialog

class ARGS_FRAME(ttk.Frame):
    """ 参数框架 """
    def __init__(self, F, choices, callback_FormCommand):
        super().__init__(F)
        
        self.create_widgets(choices, callback_FormCommand)
        
    def create_widgets(self, choices, callback_FormCommand):
        # 输出位置
        self.entry_frame = ARGS_ENTRY_FRAME(self, callback_FormCommand)
        self.entry_frame.grid(row=0, column=0, sticky=tk.EW)

        # 参数指定
        self.choice_frame = ARGS_CHOICES_FRAME(
            self,
            choices,
            callback_FormCommand
        )
        self.choice_frame.grid(row=1, column=0, sticky=tk.EW)

        self.grid_columnconfigure(0, weight=1)

class ARGS_ENTRY_FRAME(ttk.Frame):
    """ 文本框指定参数 """
    def __init__(self, F, callback_FormCommand):
        super().__init__(F)
        self.callback_FormCommand=callback_FormCommand

        self.create_widgets()
    
    def create_widgets(self):
        # 标签
        ttk.Label(self, text="选择输出路径:（默认为./output）").grid(
            row=0, column=0, padx=(0, 10), sticky=tk.W
        )
        
        # 输入框
        self.output_folder = tk.StringVar()
        self.output_folder.set("./output") # 默认值为 ./output
        self.path_entry = ttk.Entry(
            self, 
            textvariable=self.output_folder,
            width=50
        )
        self.path_entry.grid(
            row=0, column=1, padx=(0, 10), sticky=tk.EW
        )
        
        # 选择按钮
        ttk.Button(
            self, 
            text="浏览...",
            command=self.select_folder
        ).grid(
            row=0, column=2, sticky=tk.W
        )
        
        self.grid_columnconfigure(1, weight=1)
        
    def select_folder(self):
        folder_path = filedialog.askdirectory(
            title="选择文件夹",
            mustexist=True  # 确保选择的是已存在的文件夹
        )
        
        if folder_path:
            self.output_folder.set(folder_path)
            self.callback_FormCommand("output_folder",folder_path)               

class ARGS_CHOICES_FRAME(ttk.Frame):
    """ 复选框指定参数 """
    def __init__(self, F, choices, callback_FormCommand): # choices:[[choice,arg,tk.BooleanVar()]]
        super().__init__(F)

        self.create_widgets(choices, callback_FormCommand)

    def create_widgets(self, choices, callback_FormCommand):
        # 参数选择按钮
        loc = 0
        ext = {}
        for index, choice in enumerate(choices):
            if choice.get("ext"):
                ext[index] = choice
                continue
            tk.Checkbutton(
                self,
                text=choice["text"],
                variable=choice["var"],
                command=lambda idx=index, ch=choice["var"]: callback_FormCommand("add_choices", idx) if ch.get() else callback_FormCommand("remove_choices", idx)
            ).grid(
                row=loc//2, column=loc%2,
                sticky=tk.W,
                padx=(0,10)
            )
            loc += 1

        loc = (loc+1) // 2

        def toggle_options(show_options, root_frame, label_frame):
            """切换选项框架的显示/隐藏状态"""
            if show_options.get():
                label_frame.grid(row=0, column=1, padx=20, sticky='we')
                root_frame.grid_rowconfigure(1, weight=1)
            else:
                label_frame.grid_forget()
                root_frame.grid_rowconfigure(1, weight=0)

        for index, choice in ext.items(): # 带额外参数的最后显示
            frame = ttk.Frame(self)
            frame.grid(
                row=loc, column=0, columnspan=2,
                sticky=tk.W,
                padx=(0,10)
            )
            ext_frame = ttk.LabelFrame(frame, text=choice["ext_text"], padding=(10, 5))
            ext_frame.grid_forget()
            for i, (key, var) in enumerate(choice["ext"].items()):
                tk.Checkbutton(
                    ext_frame,
                    text=key,
                    variable=var,
                    command=lambda idx=index, ch=choice["var"]: callback_FormCommand("pro_choices_with_ext", idx)
                ).grid(
                    row=0, column=i+1,
                    sticky=tk.W,
                    padx=(0,10)
                )
            tk.Checkbutton(
                frame,
                text=choice["text"],
                variable=choice["var"],
                command=lambda c=choice["var"], ext_frame=ext_frame:toggle_options(c, frame, ext_frame)
            ).grid(
                row=0, column=0,
                sticky=tk.W,
                padx=(0,10)
            )

            loc += 1