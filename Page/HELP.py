from . import tk, ttk
import subprocess

class HELP(ttk.Frame):
    def __init__(self, N):
        super().__init__(N)

        self.error_msg = "错误：未检测到RePKG可执行文件。\n请将repkg.exe拖动到当前目录下或添加到环境中。"
        self.error_msg2 = "错误：{}。请尝试重新下载repkg.exe。"
        self.success_msg = "检测到RePKG版本 {}\n提交哈希值 {}。"

        self.create_widgets()

    def create_widgets(self):
        self.version_frame = ttk.LabelFrame(self, text="版本信息")
        self.version_frame.grid(
            row=0, column=0,
            sticky=tk.EW,
            padx=10, pady=10
        )
        self.version_label = ttk.Label(self.version_frame)
        self.version_label.grid(
            row=0, column=0, 
            sticky=tk.W, 
            padx=10, pady=10
        )
        self.check_repkg_version()
        ttk.Button(self.version_frame, text="刷新", command=self.check_repkg_version).grid(
            row=0, column=1,
            sticky=tk.E,
            padx=10, pady=10
        )

        self.guide_frame = ttk.LabelFrame(self, text="使用指南")
        self.guide_frame.grid(
            row=1, column=0,
            sticky=tk.EW,
            padx=10, pady=10
        )
        self.guide_text = ttk.Label(self.guide_frame, text="测试")
        self.guide_text.grid(
            row=0, column=0,
            sticky=tk.W,
            padx=10, pady=10
        )

    def check_repkg_version(self):
        try:
            result = subprocess.run(
                [".\\RePKG", "version"],
                capture_output=True,
                text=True,
                check=True
            )
            
            output = result.stderr.strip()
            if not output.startswith("RePKG"):
                raise Exception(result.stderr.strip())
            output = output.split(" ")[1]
            self.version_label.config(text=self.success_msg.format(*output.split("+")))

        except FileNotFoundError:
            self.version_label.config(text=self.error_msg)

        except Exception as e:
            self.version_label.config(text=self.error_msg2.format(str(e)))