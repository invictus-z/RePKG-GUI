from . import tk, ttk
from . import INPUT_FRAME, OUTPUT_FRAME

from abc import abstractmethod
import subprocess

class EXTRACTOR(ttk.Frame):
    def __init__(self, N):
        super().__init__(N)
        self.grid_columnconfigure(0, weight=1)

        self.input_frame = INPUT_FRAME(self, self.extractor_exec)
        self.input_frame.grid(row=0, column=0, sticky=tk.EW)

        self.output_frame = OUTPUT_FRAME(self)
        self.output_frame.grid(row=1, column=0, sticky=tk.EW)

        self.args = []

    @abstractmethod
    def extractor_exec(self):
        pass


# 继承EXTRACTOR的两个子类构建选项卡的两部分
class SINGLE_EXTRACTOR(EXTRACTOR):
    def __init__(self, N):
        super().__init__(N)
        self.input_frame.file_frame.label.config(text="选择PKG文件:")
        N.add(self, text="Single Extract")

        # 改写命令行语句

    def extractor_exec(self):
        self.output_frame.show_image()
        # 维护一个参数列表 self.input_frame.
        
        '''
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
        '''

class MULTI_EXTRACTOR(EXTRACTOR):
    def __init__(self, N):
        super().__init__(N)
        self.input_frame.file_frame.label.config(text="选择文件夹:")
        N.add(self, text="Multi Extract")

        # 改写命令行语句
    def extractor_exec(self):
        pass