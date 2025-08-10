from . import tk, ttk

class CONTACT(ttk.Frame):
    """ 联系作者 """
    def __init__(self, N, AUTHOR_EMAIL, AUTHOR_NAME="default", text=''): # name & email
        super().__init__(N)

        self.create_widgets(AUTHOR_EMAIL, AUTHOR_NAME, text)

    def create_widgets(self, AUTHOR_EMAIL, AUTHOR_NAME, text):
        ttk.Label(self,
                  text=f"created by {AUTHOR_NAME} <{AUTHOR_EMAIL}>" 
                  if AUTHOR_EMAIL else f"created by {AUTHOR_NAME}"
        ).grid(
            row=0, column=0, 
            sticky=tk.W, 
            padx=10, pady=10
        )

        if text:
            ttk.Label(self,
                  text=text
            ).grid(
                row=1, column=0, 
                sticky=tk.W, 
                padx=10, pady=10
            )
