import passed_exams_view
import tkinter
import tkinter.font as font
from tkinter import ttk
import selenium_driver
import prediction_view
import settings_view

class Menu:
    def __init__(self, new_driver):
        self.driver = new_driver
        self.initialize_window()

    def initialize_window(self):
        root = tkinter.Tk(className=" Menu")
        root.geometry('250x330')
        root.resizable(False, False)
        root.eval('tk::PlaceWindow . center')

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        lbl_font = font.Font(size=20)
        btn_font = font.Font(size=15)

        global_frame = ttk.Frame(root, padding=10)

        menu_lbl = ttk.Label(global_frame, text='Menu', font=lbl_font)
        menu_lbl.pack(side=tkinter.TOP, pady=10)

        menu_frame = ttk.Frame(global_frame)
        btn_average = tkinter.Button(menu_frame, text="Current average", pady=5,
                                     command=lambda: self.call_passed_exams())
        btn_average['font'] = btn_font
        btn_average.grid(row=0, column=0, sticky=tkinter.EW, pady=5)

        btn_predict = tkinter.Button(menu_frame, text="Predict average", pady=5,
                                     command=lambda: self.call_prediction())
        btn_predict['font'] = btn_font
        btn_predict.grid(row=1, column=0, sticky=tkinter.EW, pady=5)

        btn_settings = tkinter.Button(menu_frame, text="Settings", pady=5,
                                      command=lambda: self.call_settings())
        btn_settings['font'] = btn_font
        btn_settings.grid(row=2, column=0, sticky=tkinter.EW, pady=5)

        btn_exit = tkinter.Button(menu_frame, text="Exit", pady=5, command=lambda: self.call_shutdown())
        btn_exit['font'] = btn_font
        btn_exit.grid(row=3, column=0, sticky=tkinter.EW, pady=5)

        global_frame.pack()
        menu_frame.pack(side=tkinter.BOTTOM)
        root.protocol("WM_DELETE_WINDOW", self.call_shutdown)

        root.mainloop()

    def call_passed_exams(self):
        pe = passed_exams_view.PassedExams(self.driver)

    def call_prediction(self):
        pr = prediction_view.Prediction(self.driver)

    def call_settings(self):
        s = settings_view.Settings(self.driver)
        self.driver = s.driver

    def call_shutdown(self):
        self.driver.shutdown()
        exit(69)

if __name__ == '__main__':
    driver = selenium_driver.SeleniumDriver()
    menu = Menu(driver)
