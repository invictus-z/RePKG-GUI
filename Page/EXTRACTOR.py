from . import tk, ttk
from . import INPUT_FRAME, OUTPUT_FRAME

from abc import abstractmethod
import os, subprocess

class EXTRACTOR(ttk.Frame):
    def __init__(self, N):
        super().__init__(N)

        self.choices = [
            {
                "text" : "将所有提取的文件放在一个目录中", 
                "arg" : "--singledir", 
                "var" : tk.BooleanVar()
            },
            {
                "text" : "使用 project.json 中的名称作为项目子文件夹名",
                "arg" : "--usename",
                "var" : tk.BooleanVar()
            },
            {
                "text" : "提取 PKG 时不将 TEX 文件转换为图片",
                "arg" : "--no-tex-convert",
                "var" : tk.BooleanVar()
            }
        ]
        
        self.command = [".\\rePKG extract","","",""]

    def create_widgets(self, Itype, file_types):
        self.input_frame = INPUT_FRAME(self, self.choices, self.extractor_exec, self.form_command, Itype, file_types)
        self.input_frame.grid(row=0, column=0, sticky=tk.EW)

        self.output_frame = OUTPUT_FRAME(self, self.open_folder)
        self.output_frame.grid(row=1, column=0, sticky=tk.EW)

        self.grid_columnconfigure(0, weight=1)

    @abstractmethod
    def extractor_exec(self):
        pass

    def form_command(self, type, extra):
        if type == "input_file":
            self.command[1] = extra
        elif type == "input_file":
            self.command[1] = "-r" + extra
        elif type == "output_folder":
            self.command[2] = "-o \"" + extra + "\""
        elif type == "add_choices":
            self.command[3] += self.choices[extra]["arg"] + " "
        elif type == "remove_choices":
            self.command[3] = self.command[3].replace(self.choices[extra]["arg"] + " ", "")
        self.input_frame.command_label.config(text=f"执行语句：{' '.join(self.command)}") # 回调

        if not self.command[1]:
            self.input_frame.change_error_label("add", "WARNING: 你还未选择pkg文件")
        else:
            self.input_frame.change_error_label("remove", "WARNING: 你还未选择pkg文件")

    def open_folder(self):
        path = self.command[2][4:-1] if self.command[2].startswith("-o ") else "./output"
        if not os.path.exists(path):
            self.input_frame.change_error_label("add","WARNING: 路径不存在")
            return
            
        try:
            if os.name == 'nt':  # Windows
                os.startfile(path)
            elif os.name == 'posix' and sys.platform == 'darwin':  # macOS
                subprocess.run(['open', path])
            else:  # Linux
                subprocess.run(['xdg-open', path])
        except Exception as e:
            print(f"打开失败：{e}")


# 继承EXTRACTOR的两个子类构建选项卡的两部分
class SINGLE_EXTRACTOR(EXTRACTOR):
    def __init__(self, N):
        super().__init__(N)

        self.create_widgets(
            "file",
            [("pkg文件", "*.pkg")]
        )

        self.input_frame.file_frame.label.config(text="选择PKG文件:")
        N.add(self, text="单文件提取")

    def extractor_exec(self):
        # 维护一个参数列表 self.input_frame.        
        '''
        try:
            # example
            result = subprocess.run(
                ' '.join(self.command),
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

        删除临时文件
        '''

class MULTI_EXTRACTOR(EXTRACTOR):
    def __init__(self, N):
        super().__init__(N)

        self.create_widgets(
            "folder",
            []
        )

        self.input_frame.file_frame.label.config(text="选择文件夹:")
        N.add(self, text="多文件夹提取")

        # 改写命令行语句
    def extractor_exec(self):
        pass