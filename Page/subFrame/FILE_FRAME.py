from . import tk, ttk, filedialog

class FILE_FRAME(ttk.Frame):
    """ 输入选取框架 """
    def __init__(self, F, callback_FormCommand, Itype, file_types=[]):
        super().__init__(F)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.type = Itype
        self.file_types = file_types
        self.callback_FormCommand = callback_FormCommand
        
        self.create_widgets()

    def create_widgets(self):
        # 标签
        self.label = ttk.Label(self)
        self.label.grid(
            row=0, column=0,
            sticky=tk.W,
            padx=(0, 10)
        )

        # 文件路径输入框
        self.input_loc = tk.StringVar()
        ttk.Entry(
            self,
            textvariable=self.input_loc,
            width=50
        ).grid(
            row=0, column=1,
            sticky=tk.EW,
            padx=(0, 10)
        )

        # 选择文件按钮
        ttk.Button(
            self,
            text="浏览...",
            command=self.select
        ).grid(
            row=0, column=2,
            sticky=tk.W
        )

        self.grid_columnconfigure(1, weight=1)
    
    def select(self):
        if self.type == "file":
            self.select_file()
        elif self.type == "folder":
            self.select_folder()

    # 文件选取 
    def select_file(self):
        """打开文件选择对话框并更新路径"""
        file_path = filedialog.askopenfilename(
            title="选择文件",
            filetypes=self.file_types
        )
        
        if file_path:  # 如果用户选择了文件（未取消）
            self.input_loc.set(file_path)
            self.callback_FormCommand("input_file",file_path)        

    # 文件夹选取
    def select_folder(self):
        folder_path = filedialog.askdirectory(
            title="选择文件夹",
            mustexist=True  # 确保选择的是已存在的文件夹
        )
        
        if folder_path:
            self.input_loc.set(folder_path)
            self.callback_FormCommand("input_folder",folder_path)        