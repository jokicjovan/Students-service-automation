import tkinter
import selenium_driver
from tkinter import *
import tkinter.font as font


class Settings:
    def __init__(self, new_driver):
        self.driver = new_driver
        self.initialize_window()

    def initialize_window(self):
        root = tkinter.Tk(className=" Settings")
        root.geometry('280x230')
        root.resizable(False, False)
        root.eval('tk::PlaceWindow . center')
        lbl_font = font.Font(size=14)

        index_mark_lbl = tkinter.Label(root, text="Reg. book: ", font=lbl_font)
        index_num_lbl = tkinter.Label(root, text="Index Num.: ", font=lbl_font)
        index_year_lbl = tkinter.Label(root, text="Index Year: ", font=lbl_font)
        password_lbl = tkinter.Label(root, text="Password: ", font=lbl_font)
        index_rb = Text(root, height=1, width=15)
        index_num = Text(root, height=1, width=15)
        index_year = Text(root, height=1, width=15)
        password = Text(root, height=1, width=15)
        btn_exit = tkinter.Button(root, text="Confirm", pady=5,
                                  command=lambda: self.update_driver(root, index_rb.get("1.0", "end-1c"),
                                                                     index_num.get("1.0", "end-1c"),
                                                                     index_year.get("1.0", "end-1c"),
                                                                     password.get("1.0", "end-1c")))
        btn_exit['font'] = lbl_font

        index_mark_lbl.grid(row=0, column=0, sticky=tkinter.EW, pady=5, padx=5)
        index_num_lbl.grid(row=1, column=0, sticky=tkinter.EW, pady=5, padx=5)
        index_year_lbl.grid(row=2, column=0, sticky=tkinter.EW, pady=5, padx=5)
        password_lbl.grid(row=3, column=0, sticky=tkinter.EW, pady=5, padx=5)
        index_rb.grid(row=0, column=1, sticky=tkinter.EW, pady=5, padx=5)
        index_num.grid(row=1, column=1, sticky=tkinter.EW, pady=5, padx=5)
        index_year.grid(row=2, column=1, sticky=tkinter.EW, pady=5, padx=5)
        password.grid(row=3, column=1, sticky=tkinter.EW, pady=5, padx=5)
        btn_exit.grid(row=4, column=0, sticky=tkinter.EW, pady=5, padx=10, columnspan=2, ipady=0)

        index_rb.insert("end-1c", self.driver.index_rb)
        index_num.insert("end-1c", self.driver.index_num)
        index_year.insert("end-1c", self.driver.index_year)
        password.insert("end-1c", self.driver.password)

        root.mainloop()

    def update_driver(self, root, index_rb, index_num, index_year, password):
        self.driver.change_user(index_rb, index_num, index_year, password)
        root.destroy()
