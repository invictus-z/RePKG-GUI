from . import tk, ttk
from . import INPUT_FRAME, OUTPUT_FRAME

from PIL import Image, ImageTk
import os, subprocess

class INFO(ttk.Frame):
    def __init__(self, N):
        super().__init__(N)

        self.choices = [
            {
                "text" : "按字母顺序排序", 
                "arg" : "--sort", 
                "var" : tk.BooleanVar()
            },
            {
                "text" : "自定义排序（默认值：名称）",
                "arg" : "--sortby",
                "ext_text" : "排序规则",
                "ext" : {
                    "name":tk.BooleanVar(),
                    "extension":tk.BooleanVar(),
                    "size":tk.BooleanVar()
                },
                "args" : "",
                "var" : tk.BooleanVar()
            },
            {
                "text" : "从指定目录导出所有TEX文件信息",
                "arg" : "--tex",
                "var" : tk.BooleanVar()
            },
            {
                "text" : "从 project.json 中导出的键（* 表示全部）",
                "arg" : "--projectinfo",
                "ext_text" : "键名",
                "ext" : {
                    "name":tk.BooleanVar(),
                    "author":tk.BooleanVar(),
                    " / ":tk.BooleanVar(),
                    "*":tk.BooleanVar()
                },
                "args" : "",
                "var" : tk.BooleanVar()
            },
            {
                "text" : "打印包中的条目",
                "arg" : "--printentries",
                "var" : tk.BooleanVar()
            },
            {
                "text" : "标题过滤器",
                "arg" : "--tex-filter",
                "var" : tk.BooleanVar()
            }
        ]
        
        self.command = [".\\RePKG info","","","",""]
        # 基础命令 输入文件（夹） 输出位置 参数 自定义参数

        self.create_widgets(
            "file",
            [("pkg文件", "*.pkg")]
        )

        self.input_frame.file_frame.label.config(text="选择PKG文件:")

    def create_widgets(self, Itype, file_types):
        self.input_frame = INPUT_FRAME(self, self.choices, self.extractor_exec, self.form_command, Itype, file_types)
        self.input_frame.grid(row=0, column=0, sticky=tk.EW)

        self.output_frame = OUTPUT_FRAME(self, None)
        self.output_frame.grid(row=1, column=0, sticky=tk.EW)

        self.grid_columnconfigure(0, weight=1)

        # 隐藏部分多余组件
        self.input_frame.args_frame.entry_frame.grid_forget()
        self.output_frame.btn_openfolder.grid_forget()

    def extractor_exec(self):
        pass

    def form_command(self, type, extra): # 或者直接遍历实现（？
        if type == "input_file":
            self.command[1] = extra
        elif type == "output_folder":
            self.command[2] = "-o \"" + extra + "\""
        elif type == "add_choices":
            self.command[3] += self.choices[extra]["arg"] + " "
        elif type == "remove_choices":
            self.command[3] = self.command[3].replace(self.choices[extra]["arg"] + " ", "")
        elif type == "pro_choices_with_ext":
            self.command[4] = self.command[4].replace(self.choices[extra]["args"] + " ", "")
            self.choices[extra]["args"] = self.choices[extra]["arg"]
            for key, var in self.choices[extra]["ext"].items():
                if var.get():
                    self.choices[extra]["args"] += (" " + key[1:] + ",")
            if self.choices[extra]["args"] != self.choices[extra]["arg"]:
                self.choices[extra]["args"] = self.choices[extra]["args"][:-1]
                self.command[4] += self.choices[extra]["args"] + " "
        '''
        elif type == "remove_choices_with_ext":
            self.command[4] = self.command[4].replace(self.choices[extra]["args"], "")
            for key, var in self.choices[extra]["ext"].items():
                if var.get():
                    self.choices[extra]["args"] = self.choices[extra]["args"].replace(" " + key, "")
        '''
        self.input_frame.command_label.config(text=f"执行语句：{' '.join(self.command)}") # 回调

        if not self.command[1]:
            self.input_frame.change_error_label("add", "WARNING: 你还未选择pkg文件")
        else:
            self.input_frame.change_error_label("remove", "WARNING: 你还未选择pkg文件")