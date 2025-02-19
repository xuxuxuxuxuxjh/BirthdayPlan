# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plan_page.ui'
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
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

class PlanPage(object):
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
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 160, 388, 178))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.next_birthday_year = QSpinBox(self.layoutWidget)
        self.next_birthday_year.setObjectName(u"next_birthday_year")
        self.next_birthday_year.setMaximum(9999)

        self.horizontalLayout.addWidget(self.next_birthday_year)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.next_birthday_month = QSpinBox(self.layoutWidget)
        self.next_birthday_month.setObjectName(u"next_birthday_month")
        self.next_birthday_month.setMinimum(1)
        self.next_birthday_month.setMaximum(12)

        self.horizontalLayout.addWidget(self.next_birthday_month)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.next_birthday_day = QSpinBox(self.layoutWidget)
        self.next_birthday_day.setObjectName(u"next_birthday_day")
        self.next_birthday_day.setMinimum(1)
        self.next_birthday_day.setMaximum(31)

        self.horizontalLayout.addWidget(self.next_birthday_day)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.gap_day = QSpinBox(self.layoutWidget)
        self.gap_day.setObjectName(u"gap_day")
        self.gap_day.setMinimum(0)
        self.gap_day.setMaximum(366)
        self.gap_day.setValue(0)

        self.horizontalLayout_2.addWidget(self.gap_day)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 410, 81, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(180, 360, 381, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.advance_day = QSpinBox(self.layoutWidget1)
        self.advance_day.setObjectName(u"advance_day")
        self.advance_day.setMinimum(0)
        self.advance_day.setMaximum(366)
        self.advance_day.setValue(0)

        self.horizontalLayout_4.addWidget(self.advance_day)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.pushButton_ = QPushButton(self.layoutWidget1)
        self.pushButton_.setObjectName(u"pushButton_")

        self.horizontalLayout_4.addWidget(self.pushButton_)

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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u6b21\u751f\u65e5\u65e5\u671f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5e74", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6708", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u65e5", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8ddd\u79bb\u4eca\u5929", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5929", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u7ee7\u7eed", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u524d\u8ba1\u5212\u5929\u6570", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5929", None))
        self.pushButton_.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
    # retranslateUi

