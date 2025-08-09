from . import tk, ttk
from . import FILE_FRAME, ARGS_FRAME
from PIL import Image, ImageTk
import subprocess

class INPUT_FRAME(ttk.Frame):
    """ 输入框架 """
    def __init__(self, F, callback_exec=None):
        super().__init__(F)
        self.grid_columnconfigure(0, weight=1)
        self.callback_exec = callback_exec

        self.file_frame = FILE_FRAME(self, self.change_result_label, self.form_command)
        self.file_frame.grid(row=0, column=0, sticky=tk.EW)

        self.choices = [
            ["将所有提取的文件放在一个目录中", "--singledir", tk.BooleanVar()],
            ["使用 project.json 中的名称作为项目子文件夹名", "--usename", tk.BooleanVar()],
            ["提取 PKG 时不将 TEX 文件转换为图片", "--no-tex-convert", tk.BooleanVar()]
        ]
        self.command = [".\\rePKG extract","","",""]
        self.command_label = tk.Label(self, text="执行语句：")
        self.args_frame = ARGS_FRAME(self, self.choices, self.form_command)
        self.args_frame.grid(row=1, column=0, sticky=tk.EW)

        self.result_label = tk.Label(self, text="WARNING: 你还未选择pkg文件")
        self.result_label.grid(
            row=2, column=0, 
            sticky=tk.W,
            padx=(10, 0)
        )
        self.command_label.grid(
            row=3, column=0, 
            sticky=tk.W,
            padx=(10, 0)
        )
        tk.Button(self, text="提取", command=self.on_button_click).grid(
            row=2, column=1, 
            sticky=tk.E
        )

    def on_button_click(self):
        pass
        # self.callback_exec()

    def change_result_label(self, text):
        self.result_label.config(text=text)

    def form_command(self, type, extra=""):
        if type == "input_filename":
            pass
        elif type == "output_folder":
            self.command[2]="-o " + extra
        elif type == "choices":
            for choice in self.choices:
                args = ""
                if choice[2].get():
                    args+=choice[1]
                self.command[3] = args[:-1]
        self.command_label.config(text=f"执行语句：{' '.join(self.command)}") # 回调

# 输出框架
class OUTPUT_FRAME(ttk.Frame):
    def __init__(self, F):
        super().__init__(F)
        tk.Label(self, text="预览显示:").grid(
            row=0, column=0,
            sticky=tk.W
        )
        tk.Button(self, text="在文件夹中打开").grid(
            row=0, column=1,
            sticky=tk.E
        )
    
    def show_image(self, pid):
        # 图片预览显示
        image = ImageTk.PhotoImage(Image.open("temp\\test.png").resize((800,400)))
        label = tk.Label(self, image=image)
        label.image = image  # 保持对图片的引用，避免被垃圾回收
        label.grid(
            row=1, column=0
        )
