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
        self.error_label = ttk.Label(
            self.info_frame, 
            text="",
            wraplength=0,
            justify="left"
        )
        self.error_label.grid(
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

        self.grid_columnconfigure(0, weight=1)

    def on_button_click(self):
        pass
        # self.callback_exec() 测试阶段 暂时跳过

    def change_error_label(self, type, text): # 错误标签更新
        if type == "add":
            if text not in self.error:
                if self.error:
                    self.error += " " + text
                else:
                    self.error = text
        elif type == "remove":
            self.error = self.error.replace(f" {text}", "").replace(text, "")
        self.error_label.config(text=self.error)

        if not self.error:
            self.btn.configure(state=tk.DISABLED)
        else:
            self.btn.configure(state=tk.NORMAL)

    def update_wrap_length(self, event): # 根据窗口大小调整自动换行
        new_width = event.width

        self.command_label.config(wraplength=new_width)
        self.error_label.config(wraplength=new_width)

# 输出框架
class OUTPUT_FRAME(ttk.Frame):
    def __init__(self, F, callback_OpenFolder):
        super().__init__(F)

        self.create_widgets(callback_OpenFolder)

    def create_widgets(self, callback_OpenFolder):
        self.btn_show = ttk.Button(self, text="预览显示")
        self.btn_show.grid(
            row=0, column=0,
            sticky=tk.W,
        )
        self.btn_openfolder = ttk.Button(self, text="在文件夹中打开", command=callback_OpenFolder)
        self.btn_openfolder.grid(
            row=0, column=1,
            sticky=tk.E,
        )
    
    def show_image(self, pid):
        # 图片预览显示
        image = ImageTk.PhotoImage(Image.open("temp\\test.png").resize((800,400)))
        label = tk.Label(self, image=image)
        label.image = image  # 保持对图片的引用，避免被垃圾回收
        label.grid(
            row=1, column=0
        )