import tkinter

from tkinter import ttk
from tkinter import *
import tkinter.font as font


class PassedExams:
    def __init__(self, new_driver):
        self.driver = new_driver
        self.initialize_window()

    def initialize_window(self):
        root = tkinter.Tk(className=" Passed Exams")
        root.geometry('520x296')
        root.resizable(False, False)
        root.eval('tk::PlaceWindow . center')
        lbl_font = font.Font(size=16)
        list_frame = Frame(root, pady=20)

        scroll = Scrollbar(list_frame)
        scroll.pack(side=RIGHT, fill=Y)

        marks_preview_list = ttk.Treeview(list_frame, yscrollcommand=scroll.set)
        marks_preview_list['columns'] = ('name', 'mark', 'espb')
        marks_preview_list.column("#0", width=0, stretch=NO)
        marks_preview_list.heading("#0", text="", anchor=CENTER)
        marks_preview_list.column("name", anchor=CENTER, width=int(root.winfo_width() * 0.65))
        marks_preview_list.column("mark", anchor=CENTER, width=int(root.winfo_width() * 0.125))
        marks_preview_list.column("espb", anchor=CENTER, width=int(root.winfo_width() * 0.125))
        marks_preview_list.heading("name", text="Name", anchor=CENTER)
        marks_preview_list.heading("mark", text="Mark", anchor=CENTER)
        marks_preview_list.heading("espb", text="ESPB", anchor=CENTER)

        index = 0
        for row in self.driver.get_passed_exams():
            if index % 2 == 0:
                marks_preview_list.insert(parent='', index='end', iid=index, text='',
                                          values=(row[0], row[1], row[2]))
            else:
                marks_preview_list.insert(parent='', index='end', iid=index, text='',
                                          values=(row[0], row[1], row[2]))
            index += 1
        marks_preview_list.pack()
        list_frame.pack()
        scroll.config(command=marks_preview_list.yview)

        average_mark = "Average mark: " + str(round(self.driver.calculate_average_mark(), 2))
        espb = "ESPB: " + str(self.driver.calculate_espb())
        average_frame = Frame(root)
        average_mark_label = tkinter.Label(average_frame, text=average_mark, bg='light grey', font=lbl_font)
        average_mark_label.pack(side=tkinter.LEFT, anchor=tkinter.N, expand=1, fill=tkinter.X)
        espb_label = tkinter.Label(average_frame, text=espb, bg='light grey', font=lbl_font)
        espb_label.pack(side=tkinter.RIGHT, anchor=tkinter.N, expand=1, fill=tkinter.X)
        average_frame.pack(side=tkinter.BOTTOM, anchor=tkinter.N, expand=1, fill=tkinter.X)

        root.mainloop()
