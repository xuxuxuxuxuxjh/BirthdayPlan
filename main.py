# pip install pyside6
# pip install pyqt5-tools
# https://www.bilibili.com/video/BV1Wa41127fk?spm_id_from=333.788.videopod.episodes&vd_source=54f23b8c2e7395b9d1fda1079bfd46db
# https://www.bilibili.com/video/BV18F411W7y2/?spm_id_from=333.337.top_right_bar_window_history.content.click&vd_source=54f23b8c2e7395b9d1fda1079bfd46db
# PySide6 path: C:\Users\10733\miniconda3\Lib\site-packages\PySide6
# Pyside6-uic ui.ui -o ui.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from welcome_page import WelcomePage
from input_page import InputPage
from plan_page import PlanPage
from datetime import datetime, timedelta


def calc(birthday_year, birthday_month, birthday_day, today_year, today_month, today_day):

    # 4是为了防止出现平年29号的情况
    if datetime(4, today_month, today_day) > datetime(4, birthday_month, birthday_day):
        next_birthday_year = today_year + 1
    else:
        next_birthday_year = today_year

    while not (next_birthday_year % 4 == 0 and not next_birthday_year % 100 == 0 or next_birthday_year % 400 == 0) and birthday_month == 2 and birthday_day == 29:
        next_birthday_year = next_birthday_year + 1

    return next_birthday_year, birthday_month, birthday_day


def calc2(next_birthday_year, next_birthday_month, next_birthday_day, today_year, today_month, today_day):
    # print(next_birthday_year, next_birthday_month, next_birthday_day)
    # print(today_year, today_month, today_day)
    next_birthday = datetime(next_birthday_year, next_birthday_month, next_birthday_day)
    today = datetime(today_year, today_month, today_day)
    delta = next_birthday - today
    return delta.days


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.welcome_page = WelcomePage()
        self.input_page = InputPage()
        self.plan_page = PlanPage()

        self.birthday_day = 0
        self.birthday_month = 0
        self.birthday_year = 0
        self.today_day = 0
        self.today_month = 0
        self.today_year = 0
        self.next_birthday_year = 0
        self.next_birthday_month = 0
        self.next_birthday_day = 0
        self.gap_day = 0
        self.advance = 0
        self.advance_day = 0
        self.advance_month = 0
        self.advance_year = 0
        self.prepare_day = 0
        self.prepare_month = 0
        self.prepare_year = 0

        self.welcome_page.setupUi(self)
        self.welcome_page.pushButton.clicked.connect(self.show_input_page)

    def show_input_page(self):
        self.input_page.setupUi(self)
        self.input_page.pushButton.clicked.connect(self.show_plan_page)

    def show_plan_page(self):
        self.birthday_day = self.input_page.birthday_day.value()
        self.birthday_month = self.input_page.birthday_month.value()
        self.birthday_year = self.input_page.birthday_year.value()
        self.today_day = self.input_page.today_day.value()
        self.today_month = self.input_page.today_month.value()
        self.today_year = self.input_page.today_year.value()
        # print(self.birthday_year, self.birthday_month, self.today_day)
        # print(self.today_year, self.today_month, self.today_day)
        self.plan_page.setupUi(self)

        self.next_birthday_year, self.next_birthday_month, self.next_birthday_day = (
            calc(self.birthday_year, self.birthday_month, self.birthday_day, self.today_year, self.today_month, self.today_day))
        # print(next_birthday_year, next_birthday_month, next_birthday_day)
        self.plan_page.next_birthday_year.setValue(self.next_birthday_year)
        self.plan_page.next_birthday_month.setValue(self.next_birthday_month)
        self.plan_page.next_birthday_day.setValue(self.next_birthday_day)

        self.gap_day = calc2(self.next_birthday_year, self.next_birthday_month, self.next_birthday_day, self.today_year, self.today_month, self.today_day)
        self.plan_page.gap_day.setValue(self.gap_day)

        self.plan_page.pushButton_.clicked.connect(lambda: self.show_textBrowser())
        # self.plan_page.pushButton.clicked.connect(lambda: self.show_result_page())

    def show_textBrowser(self):
        self.advance = self.plan_page.advance_day.value()
        day = datetime(self.next_birthday_year, self.next_birthday_month, self.next_birthday_day)
        day -= timedelta(days=self.advance)
        self.advance_year = day.year
        self.advance_month = day.month
        self.advance_day = day.day
        output = f'计划为{self.advance_year}年{self.advance_month}月{self.advance_day}日'
        if day.strftime("%A") == "Monday":
            day = day - timedelta(days=2)
            output += f"星期一，由于是工作日，改为{day.year}年{day.month}月{day.day}日星期六"
        elif day.strftime("%A") == "Tuesday":
            day = day - timedelta(days=3)
            output += f"星期二，由于是工作日，改为{day.year}年{day.month}月{day.day}日星期六"
        elif day.strftime("%A") == "Wednesday":
            day = day + timedelta(days=3)
            output += f"星期三，由于是工作日，改为{day.year}年{day.month}月{day.day}日星期六"
        elif day.strftime("%A") == "Thursday":
            day = day + timedelta(days=2)
            output += f"星期四，由于是工作日，改为{day.year}年{day.month}月{day.day}日星期六"
        elif day.strftime("%A") == "Friday":
            day = day + timedelta(days=1)
            output += f"星期五，由于是工作日，改为{day.year}年{day.month}月{day.day}日星期六"
        elif day.strftime("%A") == "Saturday":
            output += "星期六"
        else:
            output += "星期天"

        self.prepare_day = day.day
        self.prepare_month = day.month
        self.prepare_year = day.year

        self.plan_page.textBrowser.setText(output)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()