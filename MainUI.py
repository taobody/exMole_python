# -*- coding:utf-8 -*-

import os
import tkinter as tk
from functools import partial
from tkinter import BOTH, StringVar, filedialog
from tkinter.ttk import Frame, Button, Style, Label, Entry, Radiobutton, Separator

import MergeBl


class MainUI(Frame):

    # main window initialize
    def __init__(self, master=None):
        super().__init__(master)
        self.base_var = StringVar(value="lidar")
        self.style = Style()
        self.init_ui()

    def init_ui(self):

        self.style.theme_use("default")

        self.master.title("Merge Data")
        self.master.geometry("800x350+300+300")
        self.master.resizable(width=0, height=0)
        # self.master.iconbitmap('merge.ico')

        # 1行目
        self.lbl_enc_path = Label(self, text="エンコーダーログ >>", anchor="e")
        self.txt_enc_path = Entry(self)
        self.btn_enc_path = Button(self, text="参　照", command=partial(self.open_dir, 'enc'))

        # 2行目
        self.lbl_lidar_path = Label(self, text="レーザーログ >>", anchor="e")
        self.txt_lidar_path = Entry(self)
        self.btn_lidar_path = Button(self, text="参　照", command=partial(self.open_dir, 'lidar'))

        # 3行目
        self.lbl_merge_base = Label(self, text="結合の基準:", anchor="e")
        self.rdb_lidar_on = Radiobutton(self, text="レーザー", value="lidar", variable=self.base_var)
        self.rdb_enc_on = Radiobutton(self, text="エンコーダー", value="enc", variable=self.base_var)
        self.btn_merge = tk.Button(self, text="結　合", fg="#000", bg="#fff8d6", command=self.merge_log)

        # separator
        self.sep_line = Separator(self, orient=tk.HORIZONTAL)

        # 4行目
        self.lbl_septarget_path = Label(self, text="分割対象ファイル >>", anchor="e")
        self.txt_septarget_path = Entry(self)
        self.btn_septarget_path = Button(self, text="参　照", command=partial(self.open_dir, 'sep_target'))

        # 5行目
        self.lbl_sep_pitch = Label(self, text="分割ピッチ >>", anchor="e")
        self.txt_sep_pitch = Entry(self, justify="right")
        self.lbl_sep_unit = Label(self, text="cm")

        # 6行目
        self.lbl_offset = Label(self, text="オフセット >>", anchor="e")
        self.txt_offset = Entry(self, justify="right")
        self.lbl_offset_unit = Label(self, text="cm")
        self.btn_sep = tk.Button(self, text="分　割", fg="#000", bg="#fff8d6")

        # 7行目
        self.btn_quit = tk.Button(self, text="閉じる", command=self.quit)

        # 配置
        self.lbl_enc_path.place(x=15, y=10, width=140, height=30)
        self.txt_enc_path.place(x=165, y=10, width=480, height=30)
        self.btn_enc_path.place(x=665, y=10, width=120, height=30)

        self.lbl_lidar_path.place(x=15, y=50, width=140, height=30)
        self.txt_lidar_path.place(x=165, y=50, width=480, height=30)
        self.btn_lidar_path.place(x=665, y=50, width=120, height=30)

        self.lbl_merge_base.place(x=260, y=100, width=140, height=30)
        self.rdb_lidar_on.place(x=425, y=100, height=30)
        self.rdb_enc_on.place(x=535, y=100, height=30)
        self.btn_merge.place(x=665, y=100, width=120, height=30)

        self.sep_line.place(x=10, y=150, width=780)

        self.lbl_septarget_path.place(x=15, y=160, width=140, height=30)
        self.txt_septarget_path.place(x=165, y=160, width=480, height=30)
        self.btn_septarget_path.place(x=665, y=160, width=120, height=30)

        self.lbl_sep_pitch.place(x=15, y=210, width=140, height=30)
        self.txt_sep_pitch.place(x=165, y=210, width=90, height=30)
        self.txt_sep_pitch.insert(tk.END, "0")
        self.lbl_sep_unit.place(x=260, y=210, width=35, height=30)

        self.lbl_offset.place(x=15, y=260, width=140, height=30)
        self.txt_offset.place(x=165, y=260, width=90, height=30)
        self.txt_offset.insert(tk.END, "0")
        self.lbl_offset_unit.place(x=260, y=260, width=35, height=30)
        self.btn_sep.place(x=665, y=260, width=120, height=30)

        self.btn_quit.place(x=665, y=310, width=120, height=30)

        self.pack(fill=BOTH, expand=1)

# event callback function

    def open_dir(self, key):

        # open file dialog and select file
        file_type = [("", "*")]
        base_dir = 'C:\\'

        if (self.txt_enc_path.get() != '') or (self.txt_lidar_path.get() != ''):
            if self.txt_enc_path.get() != '':
                base_dir = os.path.dirname(self.txt_enc_path.get())
            else:
                base_dir = os.path.dirname(self.txt_lidar_path.get())

        file_path = filedialog.askopenfilename(filetypes=file_type, initialdir=base_dir)
        target_dir = os.path.dirname(file_path)
        print(file_path)

        # set file path into Entry
        if key == 'enc':
            txt_path = self.txt_enc_path.get()
            self.txt_enc_path.delete(0, tk.END)
            self.txt_enc_path.insert(tk.END, file_path)

        elif key == 'lidar':
            txt_path = self.txt_lidar_path.get()
            self.txt_lidar_path.delete(0, tk.END)
            self.txt_lidar_path.insert(tk.END, file_path)

        elif key == 'sep_target':
            txt_path = self.txt_septarget_path.get()
            self.txt_septarget_path.delete(0, tk.END)
            self.txt_septarget_path.insert(tk.END, file_path)

    # merge log files
    def merge_log(self):
        enc_log_path = self.txt_enc_path.get()
        lidar_log_path = self.txt_lidar_path.get()

        save_dir = os.path.dirname(enc_log_path)

        MergeBl.merge(enc_log_path, lidar_log_path, save_dir)


def main():

    app = MainUI()

    # main window run
    app.mainloop()


if __name__ == '__main__':
    main()
