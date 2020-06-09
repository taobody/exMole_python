# -*- coding:utf-8 -*-

from tkinter import BOTH
from tkinter import Tk
from tkinter.ttk import Frame, Button, Style


class MainUI(Frame):

    # main window initialize
    def __init__(self):
        super().__init__()
        self.style = Style()
        self.init_ui()

    def init_ui(self):

        self.style.theme_use("default")

        self.master.title("Merge Data")
        self.pack(fill=BOTH, expand=1)

        # add button
        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.place(x=50, y=50)

def main():

    root = Tk()
    root.geometry("800x200+300+300")
    app = MainUI()

    # main window run
    root.mainloop()

# # label
# lbl_enc_path = tkinter.Label(text='エンコーダーログ　>>')
# lbl_enc_path.place(x=20, y=20)
# lbl_enc_path.pack()
#
# # entry
# txt_enc_path = tkinter.Entry(width=80)
# txt_enc_path.pack()

if __name__ == '__main__':
    main()