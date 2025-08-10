''' structure
extractor
    - input_frame
        - {file_frame}
        - {args_frame
            - args_entry_frame
            - args_choices_frame
            }
    - output_frame
        - {diag_frame}
convertor
    - input_frame
    - output_frame
info
    - input_frame
        - {file_frame}
    - output_frame
        - {diag_frame}

'''

import tkinter as tk
from tkinter import ttk, filedialog


## 调用
from .subFrame import INPUT_FRAME, OUTPUT_FRAME

## 实现
from .EXTRACTOR import SINGLE_EXTRACTOR, MULTI_EXTRACTOR
from .CONVERTOR import CONVERTOR
# from INFO import
from .CONTACT import CONTACT