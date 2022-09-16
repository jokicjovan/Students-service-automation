import tkinter

from tkinter import messagebox, ttk
from tkinter import *
import tkinter.font as font


class Prediction:
    def __init__(self, new_driver):
        self.driver = new_driver
        self.remaining_exams = self.driver.get_remaining_exams()
        self.average_mark_label = None
        self.espb_label = None
        self.initialize_window()

    def initialize_window(self):
        root = tkinter.Tk(className=" Prediction")
        root.geometry('520x340')
        root.resizable(False, False)
        root.eval('tk::PlaceWindow . center')
        lbl_font = font.Font(size=16)
        list_frame = Frame(root, pady=15)

        scroll = Scrollbar(list_frame)
        scroll.pack(side=RIGHT, fill=Y)

        marks_preview_list = ttk.Treeview(list_frame, yscrollcommand=scroll.set, selectmode='browse')
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
        for row in self.remaining_exams:
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

        predict_frame = Frame(root)
        mark_selector = Spinbox(predict_frame, from_=5, to=10, width=3)
        btn_predict = tkinter.Button(predict_frame, text="Predict", command=lambda: self.update_predict(
            marks_preview_list, mark_selector))
        mark_selector.pack(side=tkinter.LEFT, pady=15, padx=5)
        btn_predict.pack(side=tkinter.LEFT, pady=15, padx=5)
        average_mark, espb = self.calculate_average_mark()
        average = "Average mark: " + str(average_mark)
        espb = "ESPB: " + str(espb)
        average_frame = Frame(root)
        self.average_mark_label = tkinter.Label(average_frame, text=average, bg='light grey', font=lbl_font)
        self.average_mark_label.pack(side=tkinter.LEFT, anchor=tkinter.N, expand=1, fill=tkinter.X)
        self.espb_label = tkinter.Label(average_frame, text=espb, bg='light grey', font=lbl_font)
        self.espb_label.pack(side=tkinter.RIGHT, anchor=tkinter.N, expand=1, fill=tkinter.X)
        average_frame.pack(side=tkinter.BOTTOM, anchor=tkinter.N, expand=1, fill=tkinter.X)
        predict_frame.pack(side=tkinter.BOTTOM, anchor=tkinter.CENTER)

        root.mainloop()

    def update_predict(self, tree, mark_selector):
        cur_item = tree.focus()
        item = tree.item(cur_item)['values'][0]
        for exam in self.remaining_exams:
            if exam[0] == item:
                exam[1] = eval(mark_selector.get())
                break
        average_mark, espb = self.calculate_average_mark()
        var = IntVar(mark_selector)
        var.set(5)
        mark_selector.config(textvariable=var)
        mark_lbl = StringVar(self.average_mark_label)
        mark_lbl.set("Average mark: " + str(average_mark))
        self.average_mark_label.config(textvariable=mark_lbl)
        espb_lbl = StringVar(self.average_mark_label)
        espb_lbl.set("ESPB: " + str(espb))
        self.espb_label.config(textvariable=espb_lbl)
        self.refresh_tree_view(tree)

    def calculate_average_mark(self):
        passed_exams = self.driver.get_passed_exams()
        for exam in self.remaining_exams:
            if exam[1] != 5:
                passed_exams.append(exam)
        sum_marks = 0
        sum_espb = 0
        for exam in passed_exams:
            sum_marks += exam[1]
            sum_espb += exam[2]
        return round(sum_marks / len(passed_exams), 2), sum_espb

    def refresh_tree_view(self, tree):
        tree.delete(*tree.get_children())
        index = 0
        for row in self.remaining_exams:
            if index % 2 == 0:
                tree.insert(parent='', index='end', iid=index, text='',
                            values=(row[0], row[1], row[2]))
            else:
                tree.insert(parent='', index='end', iid=index, text='',
                            values=(row[0], row[1], row[2]))
            index += 1
