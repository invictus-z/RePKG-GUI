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
from tkinter import ttk

from .subFrame import FILE_FRAME, ARGS_FRAME

from .EXTRACTOR import SINGLE_EXTRACTOR, MULTI_EXTRACTOR
# from .CONVERTOR import
# from INFO import
from .CONTACT import CONTACT