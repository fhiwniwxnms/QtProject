# import sqlite3
# import sys
#
# from pay import Ui_MainWindow
# from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog
#
#
# class Example(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         # uic.loadUi('pay.ui', self)
#         self.setupUi(self)
#         self.connect = sqlite3.connect('films_db.sqlite')
#         self.pushButton_2.clicked.connect(self.update_result)
#         self.pushButton.clicked.connect(self.save_result)
#         self.tableWidget.itemChanged.connect(self.item_changed)
#         self.modified = {}
#         self.titles = None
#
#     def update_result(self):
#         cursor = self.connect.cursor()
#         result = cursor.execute('SELECT * FROM films WHERE id=?',
#                                 (item_id := self.spinBox.text(),)).fetchall()
#
#         self.tableWidget.setRowCount(len(result))
#
#         if not result:
#             self.statusBar().showMessage('Ничего не нашлось')
#             return
#         else:
#             self.statusBar().showMessage(f'Нашлись записи с id = {item_id}')
#
#         self.tableWidget.setColumnCount(len(result[0]))
#         self.titles = [desc[0] for desc in cursor.description]
#         for i, row in enumerate(result):
#             for j, val in enumerate(row):
#                 self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
#
#     def item_changed(self, item):
#         self.modified[self.titles[item.column()]] = item.text()
#
#     def save_result(self):
#         if self.modified:
#             cursor = self.connect.cursor()
#             request = 'UPDATE films SET '
#             request += ', '.join([f"{key}='{self.modified.get(key)}'"
#                                   for key in self.modified.keys()])
#             request += 'WHERE id = ?'
#             print(request)
#             cursor.execute(request, (self.spinBox.text(),))
#             self.connect.commit()
#             self.modified.clear()
#
#     def remove_results(self):
#         answer, ok_pressed = QInputDialog.getItem(
#             self, 'Подтверждение удаления', 'Вы точно хотите удалить элемент(ы)?', ('Нет', 'Да'), 1, False
#         )
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec())



# CREATE TABLE expences (
#     ID          INTEGER PRIMARY KEY AUTOINCREMENT
#                         UNIQUE
#                         NOT NULL,
#     Category    TEXT    NOT NULL,
#     Description TEXT    NOT NULL,
#     Balance     REAL    NOT NULL,
#     Status      TEXT    NOT NULL
# );