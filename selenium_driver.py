from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class SeleniumDriver:
    def __init__(self, index_rb, index_num, index_year, password):
        self.index_rb = index_rb
        self.index_year = index_year
        self.index_num = index_num
        self.password = password
        self.driver = self.setup_driver()

    def __init__(self):
        file=open("login_data.txt")
        credentials=file.readline().split('|')
        file.close()
        self.index_rb = credentials[0]
        self.index_num = credentials[1]
        self.index_year = credentials[2]
        self.password = credentials[3]
        self.driver = self.setup_driver()


    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        #options.add_argument('--headless')
        options.add_argument('--incognito')
        new_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        new_driver.get("https://ssluzba.ftn.uns.ac.rs/ssluzbasp/do")

        specialization = new_driver.find_element(by=By.ID, value="maticnaKnjiga")
        specialization.send_keys(self.index_rb)

        num_in_year = new_driver.find_element(by=By.ID, value="brojUGodini")
        num_in_year.send_keys(self.index_num)

        year = new_driver.find_element(by=By.ID, value="godinaUpisa")
        year.send_keys(self.index_year)

        password = new_driver.find_element(by=By.ID, value="pass")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        return new_driver

    def get_passed_exams(self):
        passed_exams_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Положени предмети")))
        passed_exams_link.click()
        self.driver.switch_to.frame('frame1')
        passed_exams = []
        elements = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, '//table/tbody/tr/td')))
        i = 10
        while i < len(elements) - 3:  # 8 for header and 3 for footer
            passed_exams.append([elements[i].text, eval(elements[i + 4].text), eval(elements[i + 1].text)])
            i += 8
        self.driver.switch_to.parent_frame()
        return passed_exams

    def get_remaining_exams(self):
        remaining_exams_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Неположени испити")))
        remaining_exams_link.click()
        self.driver.switch_to.frame('frame1')

        remaining_exams = []
        elements = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, '//table/tbody/tr/td')))
        i = 12
        while i < len(elements):
            remaining_exams.append([elements[i].text, 5, eval(elements[i + 5].text)])
            i += 10
        self.driver.switch_to.parent_frame()
        return remaining_exams

    def calculate_average_mark(self):
        sum_marks = 0
        counter = 0
        for exam in self.get_passed_exams():
            sum_marks += exam[1]
            counter += 1
        return sum_marks / counter

    def calculate_espb(self):
        sum_espb = 0
        for exam in self.get_passed_exams():
            sum_espb += exam[2]
        return sum_espb

    def shutdown(self):
        link = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, ":: Одјава")))
        link.click()
        self.driver.quit()

    def change_user(self, index_rb, index_num, index_year, password):
        link = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, ":: Одјава")))
        link.click()

        self.index_rb = index_rb
        self.index_year = index_year
        self.index_num = index_num
        self.password = password
        file=open("login_data.txt",'w')
        file.write(index_rb+"|"+index_num+"|"+index_year+"|"+password)
        file.close()

        self.driver.get("https://ssluzba.ftn.uns.ac.rs/ssluzbasp/do")

        specialization = self.driver.find_element(by=By.ID, value="maticnaKnjiga")
        specialization.send_keys(self.index_rb)

        num_in_year = self.driver.find_element(by=By.ID, value="brojUGodini")
        num_in_year.send_keys(self.index_num)

        year = self.driver.find_element(by=By.ID, value="godinaUpisa")
        year.send_keys(self.index_year)

        password = self.driver.find_element(by=By.ID, value="pass")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

