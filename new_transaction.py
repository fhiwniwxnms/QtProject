# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import res_new_trans_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(473, 500)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(154, 253, 255, 255), stop:1 rgba(102, 111, 206, 255));\n"
"font-family: Cambria Math")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 451, 481))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 7px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.new_transaction = QLabel(self.frame)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setGeometry(QRect(0, 10, 451, 71))
        self.new_transaction.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.new_transaction.setStyleSheet(u"font-weight: bold;\n"
"font-size: 25pt;\n"
"background-color: none;\n"
"border: none;")
        self.new_transaction.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_choosing = QDateEdit(self.frame)
        self.date_choosing.setObjectName(u"date_choosing")
        self.date_choosing.setGeometry(QRect(110, 80, 141, 41))
        font = QFont()
        font.setFamilies([u"Cambria Math"])
        font.setPointSize(15)
        self.date_choosing.setFont(font)
        self.date_choosing.setStyleSheet(u"QDateTimeEdit::calendarPopup {\n"
"background-color: #00ff00;\n"
"color: #ff00ff;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"font-size: 15pt;\n"
"color: rgb(51, 51, 51);\n"
"background-color: white;\n"
"selection-background-color: rgb(129, 162, 199);\n"
"selection-color:rgba(230, 230, 230) ;\n"
"}")
        self.date_choosing.setDateTime(QDateTime(QDate(2024, 11, 12), QTime(17, 0, 0)))
        self.date_choosing.setCalendarPopup(True)
        self.date_choosing.setDate(QDate(2024, 11, 12))
        self.description_edit = QLineEdit(self.frame)
        self.description_edit.setObjectName(u"description_edit")
        self.description_edit.setGeometry(QRect(10, 180, 431, 81))
        self.description_edit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.description_edit.setToolTipDuration(-1)
        self.description_edit.setAutoFillBackground(False)
        self.description_edit.setStyleSheet(u"font-size: 15pt")
        self.sum_edit = QLineEdit(self.frame)
        self.sum_edit.setObjectName(u"sum_edit")
        self.sum_edit.setGeometry(QRect(10, 270, 431, 81))
        self.sum_edit.setStyleSheet(u"font-size: 15pt")
        self.increase_decrease = QComboBox(self.frame)
        self.increase_decrease.addItem("")
        self.increase_decrease.addItem("")
        self.increase_decrease.setObjectName(u"increase_decrease")
        self.increase_decrease.setGeometry(QRect(10, 360, 431, 41))
        self.increase_decrease.setStyleSheet(u"font-size: 15pt")
        self.date_label = QLabel(self.frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(270, 80, 121, 31))
        self.date_label.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"font-size: 16pt")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 420, 421, 41))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"font-size: 15pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/Add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))
        self.choosing_category = QComboBox(self.frame)
        self.choosing_category.setObjectName(u"choosing_category")
        self.choosing_category.setGeometry(QRect(10, 130, 431, 41))
        self.choosing_category.setStyleSheet(u"font-size: 15pt")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.new_transaction.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f", None))
#if QT_CONFIG(accessibility)
        self.description_edit.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.description_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u043a\u0443\u043f\u043a\u0438", None))
        self.sum_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.increase_decrease.setItemText(0, QCoreApplication.translate("Dialog", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.increase_decrease.setItemText(1, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))

        self.date_label.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.choosing_category.setCurrentText("")
        self.choosing_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
    # retranslateUi

