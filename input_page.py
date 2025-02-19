# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_page.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class InputPage(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(742, 562)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 40, 351, 151))
        font = QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 360, 81, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(150, 210, 401, 101))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.birthday_year = QSpinBox(self.layoutWidget)
        self.birthday_year.setObjectName(u"birthday_year")
        self.birthday_year.setMaximum(9999)

        self.horizontalLayout.addWidget(self.birthday_year)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.birthday_month = QSpinBox(self.layoutWidget)
        self.birthday_month.setObjectName(u"birthday_month")
        self.birthday_month.setMinimum(1)
        self.birthday_month.setMaximum(12)

        self.horizontalLayout.addWidget(self.birthday_month)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.birthday_day = QSpinBox(self.layoutWidget)
        self.birthday_day.setObjectName(u"birthday_day")
        self.birthday_day.setMinimum(1)
        self.birthday_day.setMaximum(31)

        self.horizontalLayout.addWidget(self.birthday_day)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.today_year = QSpinBox(self.layoutWidget)
        self.today_year.setObjectName(u"today_year")
        self.today_year.setMaximum(9999)

        self.horizontalLayout_2.addWidget(self.today_year)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.today_month = QSpinBox(self.layoutWidget)
        self.today_month.setObjectName(u"today_month")
        self.today_month.setMinimum(1)
        self.today_month.setMaximum(12)

        self.horizontalLayout_2.addWidget(self.today_month)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.today_day = QSpinBox(self.layoutWidget)
        self.today_day.setObjectName(u"today_day")
        self.today_day.setMinimum(1)
        self.today_day.setMaximum(31)

        self.horizontalLayout_2.addWidget(self.today_day)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 742, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u751f\u65e5\u805a\u4f1a\u8ba1\u5212\u4fbf\u7b7e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u7ee7\u7eed", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u751f\u65e5\u671f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5e74", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6708", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u65e5", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u5929\u65e5\u671f", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5e74", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6708", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u65e5", None))
    # retranslateUi

