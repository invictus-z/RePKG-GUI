from . import tk, ttk

class CONTACT(ttk.Frame):
    """ 联系作者 """
    def __init__(self, N, AUTHOR_EMAIL, AUTHOR_NAME="default"): # name & email
        super().__init__(N)

        ttk.Label(self,
                  text=f"created by {AUTHOR_NAME} <{AUTHOR_EMAIL}>" 
                  if AUTHOR_EMAIL else f"created by {AUTHOR_NAME}"
        ).grid(
            row=0, column=0, 
            sticky=tk.W, 
            padx=10, pady=10
        )
