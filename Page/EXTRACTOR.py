from . import tk, ttk
from . import FILE_FRAME, ARGS_FRAME
from PIL import Image, ImageTk
import subprocess

class EXTRACTOR():
    def __init__(self, N):
        self.frame = ttk.Frame(N)
        self.frame.grid_columnconfigure(0, weight=1)

        self.input_frame = INPUT_FRAME(self.frame, self.extractor_exec)
        self.input_frame.frame.grid(row=0, column=0, sticky=tk.EW)

        self.output_frame = OUTPUT_FRAME(self.frame)
        self.output_frame.frame.grid(row=1, column=0, sticky=tk.EW)

    def extractor_exec(self): # 回调执行
        self.output_frame.show_image()
        # 维护一个参数列表 self.input_frame.
        try:
            # example
            result = subprocess.run(
                ["ls", "-l"],
                capture_output=True,
                text=True,   
                check=True      
            )
            print("命令输出：")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"命令执行失败：{e.stderr}")
        except FileNotFoundError:
            print("错误：找不到该命令")
        except Exception as e:
            print(f"发生未知错误：{e}")

class INPUT_FRAME():
    """ 输入框架 """
    def __init__(self, F, callback_exec=None):
        self.frame = ttk.Frame(F)
        self.frame.grid_columnconfigure(0, weight=1)
        self.callback_exec = callback_exec

        self.file_frame = FILE_FRAME(self.frame, self.change_result_label)
        self.file_frame.frame.grid(row=0, column=0, sticky=tk.EW)

        self.args_frame = ARGS_FRAME(self.frame)
        self.args_frame.frame.grid(row=1, column=0, sticky=tk.EW)

        self.result_label = tk.Label(self.frame, text="WARNING: 你还未选择pkg文件")
        self.result_label.grid(
            row=2, column=0, 
            sticky=tk.W,
            padx=(10, 0)
        )
        self.command_label = tk.Label(self.frame, text="执行语句：")
        self.command_label.grid(
            row=2, column=0, 
            sticky=tk.W,
            padx=(10, 0)
        )
        tk.Button(self.frame, text="提取", command=self.on_button_click).grid(
            row=2, column=1, 
            sticky=tk.E
        )

    def on_button_click(self):
        self.form_command()
        self.callback_exec()

    def change_result_label(self, text):
        self.result_label.config(text=text)

    def form_command(self):
        self.command = ["rePKG.exe"]
        ### 语句生成
        self.command_label.config(text=f"执行语句：{' '.join(self.command)}")

# 输出框架
class OUTPUT_FRAME():
    def __init__(self, F):
        self.frame = ttk.Frame(F)
        tk.Label(self.frame, text="预览显示:").grid(
            row=0, column=0,
            sticky=tk.W
        )
        tk.Button(self.frame, text="在文件夹中打开").grid(
            row=0, column=1,
            sticky=tk.E
        )
    
    def show_image(self):
        # 图片预览显示
        image = ImageTk.PhotoImage(Image.open("temp\\test.png").resize((800,400)))
        label = tk.Label(self.frame, image=image)
        label.image = image  # 保持对图片的引用，避免被垃圾回收
        label.grid(
            row=1, column=0
        )


# 继承EXTRACTOR的两个子类构建选项卡的两部分
class SINGLE_EXTRACTOR(EXTRACTOR):
    def __init__(self, N):
        super().__init__(N)
        self.input_frame.file_frame.label.config(text="选择PKG文件:")
        N.add(self.frame, text="Single Extract")

        # 改写命令行语句

class MULTI_EXTRACTOR(EXTRACTOR):
    def __init__(self, N):
        super().__init__(N)
        self.input_frame.file_frame.label.config(text="选择文件夹:")
        N.add(self.frame, text="Multi Extract")

        # 改写命令行语句