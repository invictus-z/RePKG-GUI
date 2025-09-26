from . import tk, ttk
from . import FILE_FRAME, ARGS_FRAME
from PIL import Image, ImageTk

class INPUT_FRAME(ttk.LabelFrame):
    """ 输入框架 """
    def __init__(self, F, choices, callback_exec, callback_FormCommand, Itype, file_types):
        super().__init__(F, text='input')
        self.callback_exec = callback_exec
        self.choices = choices
        self.error = ""
        self.warning = ""

        self.create_widgets(callback_FormCommand, Itype, file_types)
        
    def create_widgets(self, callback_FormCommand, Itype, file_types):
        # 文件帧
        self.file_frame = FILE_FRAME(self, callback_FormCommand, Itype, file_types)
        self.file_frame.grid(row=0, column=0, sticky=tk.EW)

        # 参数帧
        self.args_frame = ARGS_FRAME(self, self.choices, callback_FormCommand)
        self.args_frame.grid(row=1, column=0, sticky=tk.EW)

        ttk.Separator(self, orient="horizontal").grid(
            row=2, column=0, 
            sticky="ew", padx=10, pady=5
        )

        # 回显帧
        self.info_frame = ttk.Frame(self)
        self.info_frame.grid(row=3, column=0, sticky=tk.EW)

        # 命令行回显
        self.command_label = ttk.Label(
            self.info_frame, 
            text="执行语句：",
            wraplength=0,
            justify="left"
        )
        self.command_label.grid(
            row=0, column=0, 
            sticky=tk.W,
            padx=(10, 0)
        )
        # 预警信息提示
        self.risk_label = ttk.Label(
            self.info_frame, 
            text="",
            wraplength=0,
            justify="left"
        )
        self.risk_label.grid(
            row=1, column=0,
            sticky=tk.W,
            padx=(10, 0)
        )
        self.grid_rowconfigure(1, weight=1)

        # 执行按钮
        self.btn = ttk.Button(self, text="执行", command=self.on_button_click)
        self.btn.grid(
            row=4, column=0, 
            sticky=tk.EW
        )
        self.btn.configure(state=tk.DISABLED)

        self.grid_columnconfigure(0, weight=1)

    def on_button_click(self):
        self.change_risk_label("remove", "WARNING")
        self.callback_exec()

    def change_risk_label(self, type, subtype, text=""): # 风险标签更新
        if type == "add":
            if subtype == "WARNING":
                if self.warning:
                    self.warning += " " + subtype + ":" + text
                else:
                    self.warning = subtype + ":" + text
            elif subtype == "ERROR" and text not in self.error:
                if self.error:
                    self.error += " " + subtype + ":" + text
                else:
                    self.error = subtype + ":" + text
        elif type == "remove":
            if subtype == "WARNING":
                self.warning = ""
            elif subtype == "ERROR" and text in self.error:
                self.error = self.error.replace(f" {text}", "").replace(text, "")
        self.risk_label.config(text=self.error + self.warning)

        if self.error:
            self.btn.configure(state=tk.DISABLED)
        else:
            self.btn.configure(state=tk.NORMAL)

    def update_wrap_length(self, event): # 根据窗口大小调整自动换行
        new_width = event.width

        self.command_label.config(wraplength=new_width)
        self.risk_label.config(wraplength=new_width)

# 输出框架
class OUTPUT_FRAME(ttk.Frame):
    def __init__(self, F, callback_OpenFolder, callback_FindImage):
        super().__init__(F)

        self.create_widgets(callback_OpenFolder, callback_FindImage)

    def create_widgets(self, callback_OpenFolder, callback_FindImage):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.btn_show = ttk.Button(self, text="预览显示", command=callback_FindImage)
        self.btn_show.grid(
            row=0, column=0,
            sticky=tk.W,
        )
        self.btn_openfolder = ttk.Button(self, text="在文件夹中打开", command=callback_OpenFolder)
        self.btn_openfolder.grid(
            row=0, column=1,
            sticky=tk.W,
        )
    
    def show_image(self, files, height=400):
        image = Image.open(files[0])
        width = int( image.size[0] / image.size[1] * height )
        imagetk = ImageTk.PhotoImage(image.resize((width, height)))
        label = tk.Label(self, image=imagetk)
        label.image = imagetk  # 保持对图片的引用，避免被垃圾回收
        label.grid(
            row=1, column=0, columnspan=3,
            sticky="nsew"
        )