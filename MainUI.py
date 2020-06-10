# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import BOTH, StringVar
from tkinter.ttk import Frame, Button, Style, Label, Entry, Radiobutton, Separator


class MainUI(Frame):

    # main window initialize
    def __init__(self):
        super().__init__()
        self.base_var = StringVar(value="lidar")
        self.style = Style()
        self.init_ui()
        btn_quit = tk.Button(self, text="閉じる", command=self.quit)
        btn_quit.place(x=665, y=310, width=120, height=30)

    def init_ui(self):

        self.style.theme_use("default")

        self.master.title("Merge Data")
        self.master.geometry("800x350+300+300")
        self.master.resizable(width=0, height=0)
        self.master.iconbitmap("./img/merge.ico")

        # 1行目
        lbl_enc_path = Label(self, text="エンコーダーログ >>", anchor="e")
        txt_enc_path = Entry(self)
        btn_enc_path = Button(self, text="参　照")

        # 2行目
        lbl_lidar_path = Label(self, text="レーザーログ >>", anchor="e")
        txt_lidar_path = Entry(self)
        btn_lidar_path = Button(self, text="参　照")

        # 3行目
        lbl_merge_base = Label(self, text="結合の基準:", anchor="e")
        rdb_lidar_on = Radiobutton(self, text="レーザー", value="lidar", variable=self.base_var)
        rdb_enc_on = Radiobutton(self, text="エンコーダー", value="enc", variable=self.base_var)
        btn_merge = tk.Button(self, text="結　合", fg="#000", bg="#fff8d6")

        # separator
        sep_line = Separator(self, orient=tk.HORIZONTAL)

        # 4行目
        lbl_septarget_path = Label(self, text="分割対象ファイル >>", anchor="e")
        txt_septarget_path = Entry(self)
        btn_septarget_path = Button(self, text="参　照")

        # 5行目
        lbl_sep_pitch = Label(self, text="分割ピッチ >>", anchor="e")
        txt_sep_pitch = Entry(self, justify="right")
        lbl_sep_unit = Label(self, text="cm")

        # 6行目
        lbl_offset = Label(self, text="オフセット >>", anchor="e")
        txt_offset = Entry(self, justify="right")
        lbl_offset_unit = Label(self, text="cm")
        btn_sep = tk.Button(self, text="結　合", fg="#000", bg="#fff8d6")

        # 配置
        lbl_enc_path.place(x=15, y=10, width=140, height=30)
        txt_enc_path.place(x=165, y=10, width=480, height=30)
        btn_enc_path.place(x=665, y=10, width=120, height=30)

        lbl_lidar_path.place(x=15, y=50, width=140, height=30)
        txt_lidar_path.place(x=165, y=50, width=480, height=30)
        btn_lidar_path.place(x=665, y=50, width=120, height=30)

        lbl_merge_base.place(x=260, y=100, width=140, height=30)
        rdb_lidar_on.place(x=425, y=100, height=30)
        rdb_enc_on.place(x=535, y=100, height=30)
        btn_merge.place(x=665, y=100, width=120, height=30)

        sep_line.place(x=10, y=150, width=780)

        lbl_septarget_path.place(x=15, y=160, width=140, height=30)
        txt_septarget_path.place(x=165, y=160, width=480, height=30)
        btn_septarget_path.place(x=665, y=160, width=120, height=30)

        lbl_sep_pitch.place(x=15, y=210, width=140, height=30)
        txt_sep_pitch.place(x=165, y=210, width=90, height=30)
        txt_sep_pitch.insert(tk.END, "0")
        lbl_sep_unit.place(x=260, y=210, width=35, height=30)

        lbl_offset.place(x=15, y=260, width=140, height=30)
        txt_offset.place(x=165, y=260, width=90, height=30)
        txt_offset.insert(tk.END, "0")
        lbl_offset_unit.place(x=260, y=260, width=35, height=30)
        btn_sep.place(x=665, y=260, width=120, height=30)

        self.pack(fill=BOTH, expand=1)


def main():

    app = MainUI()

    # main window run
    app.mainloop()

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