# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'expence_tracker.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1081, 768)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(154, 253, 255, 255), stop:1 rgba(102, 111, 206, 255));\n"
"font-family: Cambria Math")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 7px")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.balance_label = QLabel(self.balance_frame)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setStyleSheet(u"font-weight: bold;\n"
"font-size: 25pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.verticalLayout.addWidget(self.balance_label)

        self.balance_sum = QLabel(self.balance_frame)
        self.balance_sum.setObjectName(u"balance_sum")
        self.balance_sum.setStyleSheet(u"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.verticalLayout.addWidget(self.balance_sum)

        self.income = QHBoxLayout()
        self.income.setSpacing(0)
        self.income.setObjectName(u"income")
        self.income_icon = QLabel(self.balance_frame)
        self.income_icon.setObjectName(u"income_icon")
        self.income_icon.setMaximumSize(QSize(24, 16777215))
        self.income_icon.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px \n"
"")
        self.income_icon.setPixmap(QPixmap(u":/icons/icons/Increase.svg"))

        self.income.addWidget(self.income_icon)

        self.income_label = QLabel(self.balance_frame)
        self.income_label.setObjectName(u"income_label")
        self.income_label.setStyleSheet(u"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px \n"
"")

        self.income.addWidget(self.income_label)


        self.verticalLayout.addLayout(self.income)

        self.income_sum = QLabel(self.balance_frame)
        self.income_sum.setObjectName(u"income_sum")
        self.income_sum.setStyleSheet(u"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.verticalLayout.addWidget(self.income_sum)

        self.outcome = QHBoxLayout()
        self.outcome.setSpacing(0)
        self.outcome.setObjectName(u"outcome")
        self.outcome_icon = QLabel(self.balance_frame)
        self.outcome_icon.setObjectName(u"outcome_icon")
        self.outcome_icon.setMaximumSize(QSize(24, 16777215))
        self.outcome_icon.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px \n"
"")
        self.outcome_icon.setPixmap(QPixmap(u":/icons/icons/Decrease.svg"))

        self.outcome.addWidget(self.outcome_icon)

        self.outcome_label = QLabel(self.balance_frame)
        self.outcome_label.setObjectName(u"outcome_label")
        self.outcome_label.setStyleSheet(u"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px \n"
"")

        self.outcome.addWidget(self.outcome_label)


        self.verticalLayout.addLayout(self.outcome)

        self.outcome_sum = QLabel(self.balance_frame)
        self.outcome_sum.setObjectName(u"outcome_sum")
        self.outcome_sum.setStyleSheet(u"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.verticalLayout.addWidget(self.outcome_sum)


        self.horizontalLayout_8.addWidget(self.balance_frame)

        self.categories_frame = QFrame(self.centralwidget)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 7px")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.categories_label = QLabel(self.categories_frame)
        self.categories_label.setObjectName(u"categories_label")
        self.categories_label.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-bottom: 10px \n"
"")

        self.verticalLayout_2.addWidget(self.categories_label)

        self.categories = QVBoxLayout()
        self.categories.setObjectName(u"categories")
        self.categories_buttons = QHBoxLayout()
        self.categories_buttons.setObjectName(u"categories_buttons")
        self.category_add = QPushButton(self.categories_frame)
        self.category_add.setObjectName(u"category_add")
        self.category_add.setStyleSheet(u"margin-bottom: 10px;\n"
"margin-right: 5px ")
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.category_add.setIcon(icon)

        self.categories_buttons.addWidget(self.category_add)

        self.category_delete = QPushButton(self.categories_frame)
        self.category_delete.setObjectName(u"category_delete")
        self.category_delete.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category_delete.sizePolicy().hasHeightForWidth())
        self.category_delete.setSizePolicy(sizePolicy)
        self.category_delete.setMaximumSize(QSize(246, 16777215))
        self.category_delete.setStyleSheet(u"margin-bottom: 10px;\n"
"margin-left: 5px ")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/Undo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.category_delete.setIcon(icon1)

        self.categories_buttons.addWidget(self.category_delete)


        self.categories.addLayout(self.categories_buttons)

        self.categories_table = QTableView(self.categories_frame)
        self.categories_table.setObjectName(u"categories_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.categories_table.sizePolicy().hasHeightForWidth())
        self.categories_table.setSizePolicy(sizePolicy1)
        self.categories_table.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView:section {\n"
"background-color: rgba(53, 53, 53);\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt\n"
"}\n"
"\n"
"QTableView:item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableView:item:selected {\n"
"border: none;\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")

        self.categories.addWidget(self.categories_table)


        self.verticalLayout_2.addLayout(self.categories)


        self.horizontalLayout_8.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.transactions = QHBoxLayout()
        self.transactions.setObjectName(u"transactions")
        self.transaction_add = QPushButton(self.centralwidget)
        self.transaction_add.setObjectName(u"transaction_add")
        self.transaction_add.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/Add cart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.transaction_add.setIcon(icon2)
        self.transaction_add.setIconSize(QSize(24, 24))

        self.transactions.addWidget(self.transaction_add)

        self.transaction_edit = QPushButton(self.centralwidget)
        self.transaction_edit.setObjectName(u"transaction_edit")
        self.transaction_edit.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/Edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.transaction_edit.setIcon(icon3)
        self.transaction_edit.setIconSize(QSize(24, 24))

        self.transactions.addWidget(self.transaction_edit)

        self.transaction_delete = QPushButton(self.centralwidget)
        self.transaction_delete.setObjectName(u"transaction_delete")
        self.transaction_delete.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/Delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.transaction_delete.setIcon(icon4)
        self.transaction_delete.setIconSize(QSize(24, 24))

        self.transactions.addWidget(self.transaction_delete)


        self.verticalLayout_3.addLayout(self.transactions)

        self.transactions_table = QTableView(self.centralwidget)
        self.transactions_table.setObjectName(u"transactions_table")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.transactions_table.sizePolicy().hasHeightForWidth())
        self.transactions_table.setSizePolicy(sizePolicy2)
        self.transactions_table.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView:section {\n"
"background-color: rgba(53, 53, 53);\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt\n"
"}\n"
"\n"
"QTableView:item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableView:item:selected {\n"
"border: none;\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.transactions_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.transactions_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.transactions_table.setShowGrid(False)
        self.transactions_table.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.transactions_table)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expence Tracker", None))
        self.balance_label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.balance_sum.setText(QCoreApplication.translate("MainWindow", u"{balance}", None))
        self.income_icon.setText("")
        self.income_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.income_sum.setText(QCoreApplication.translate("MainWindow", u"{sum}", None))
        self.outcome_icon.setText("")
        self.outcome_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))
        self.outcome_sum.setText(QCoreApplication.translate("MainWindow", u"{sum}", None))
        self.categories_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0442\u0440\u0430\u0442", None))
        self.category_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.category_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.transaction_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
        self.transaction_edit.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
        self.transaction_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
    # retranslateUi

