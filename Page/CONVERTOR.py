from . import tk, ttk
from . import INPUT_FRAME, OUTPUT_FRAME

from abc import abstractmethod
import subprocess

class CONVERTOR(ttk.Frame):
    def __init__(self, N):
        super().__init__(N)
        self.grid_columnconfigure(0, weight=1)

        self.choices = []

        self.command = [".\\RePKG convert"]
        self.input_frame = INPUT_FRAME(self, self.choices, self.convertor_exec, self.form_command,
            "file",[]
        )
        self.input_frame.grid(row=0, column=0, sticky=tk.EW)
        self.input_frame.file_frame.label.config(text="选择PKG文件:")

        self.output_frame = OUTPUT_FRAME(self, None)
        self.output_frame.grid(row=1, column=0, sticky=tk.EW)

        self.args = []

    @abstractmethod
    def convertor_exec(self):
        pass

    def form_command(self, type, extra):
        pass