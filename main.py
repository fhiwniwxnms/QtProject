import sys
import sqlite3

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from expence_tracker import Ui_MainWindow
from new_transaction import Ui_Dialog


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.conn = sqlite3.connect('expence_db.sqlite')  # Подключение бд

    def add_new_transaction_request(self, date, category, description, balance, status):
        cursor = self.connect.cursor()  # Открываем курсор для работы с бд
        request = 'INSERT INTO expences (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)'
        # Запрос на добавление в таблицу бд expences значений столбцов
        cursor.execute(request, [date, category, description, balance, status])  # Выполнение запроса
        self.conn.commit()  # Фиксирование изменений бд

    def update_transaction_request(self, date, category, description, balance, status, id):
        cursor = self.connect.cursor()
        request = 'UPDATE expences SET Date=?, Category=?, Description=?, Balance=?, Status=?, WHERE ID=?'
        # Запрос на обновление даты, категории, описания, баланса и статуса транзакции по ID.
        cursor.execute(request, [date, category, description, balance, status, id])
        self.conn.commit()

    def delete_transaction_request(self, id):
        cursor = self.connect.cursor()
        request = 'DELETE FROM expences WHERE ID=?'
        # Запрос на удаление транзакции по ID
        cursor.execute(request, [id])
        self.conn.commit()

    def get_total(self, column, filter=None, value=None):
        cursor = self.connect.cursor()
        request = f'SELECT SUM ({column}) FROM expences'
        # Запрос для получения суммы по указанному столбцу
        if filter is not None and value is not None:
            request += f'WHERE {filter} = ?'
        # Условие для фильтрации по статусу, если необходимо

        request_values = [] # Подготавливаем список значений для подстановки в запрос
        if value is not None: # Добавляем значение фильтрации в список, если оно задано
            request_values.append(value)

        query = cursor.execute(request, request_values)
        # Исполняем запрос с параметрами и получаем результат

        if query.next(): # Проверяем, есть ли результат для запроса
            return str(query.value(0)) + '₽'
        # Возвращаем сумму как строку с символом валюты

        return '0'  # Если нет результата, возвращаем '0'

    def total_balance(self):
        # Метод для получения общего баланса.
        # Вызов метода get_total с указанием столбца 'Balance'
        return self.get_total(column='Balance')

    def total_income(self):
        # Метод для получения общего дохода.
        # Вызов метода get_total, фильтруя по статусу 'Income' в столбце 'Status'
        return self.get_total(column='Balance', filter='Status', value='Income')

    def total_outcome(self):
        # Метод для получения общего расхода.
        # Вызов метода get_total, фильтруя по статусу 'Outcome' в столбце 'Status'
        return self.get_total(column='Balance', filter='Status', value='Outcome')


class ExpenceTracker(QMainWindow):
    def __init__(self):
        super(ExpenceTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()  # Подключение бд

        self.ui.transaction_add.clicked.connect(self.open_new_transaction_window)
        self.ui.transaction_edit.clicked.connect(self.open_new_transaction_window)
        self.ui.transaction_delete.clicked.connect(self.delete_current_transaction)

    def view_data(self):
        self.model

    def open_new_transaction_window(self):
        self.new_transaction = QtWidgets.QDialog()
        self.ui_window.setupUi(self.new_transaction)
        self.new_transaction.show()  # Открытие окна создания/редактирования транзакции
        sender = self.sender()  # Сохранение последнего источника сигнала

        if sender.text() == 'Добавить транзакцию':
            self.ui_window.transaction_add.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.transaction_add.clicked.connect(self.edit_current_transaction())

    def add_new_transaction(self):
        date = self.ui_window.date_choosing.text()
        category = self.ui_window.choosing_category.currentText()
        description = self.ui_window.description_edit.text()
        balance = self.ui_window.sum_edit.text()
        status = self.ui_window.increase_decrease.currentText()
        # Получаем нужные нам данные (дата, категория, описание, сумму и статус)

        self.conn.add_new_transaction_request(date, category, description, balance, status)
        # Передали в метод, отвечающий за добавление новых данных в бд

        self.new_transaction.close()
        # Закрыли окно создания/редактирования транзакции

    def edit_current_transaction(self):
        index = self.ui.transactions_table.selectedIndexes()[0]  # Получаем индекс выбранной транзакции в таблице
        id = str(self.ui.transactions_table.model().data(index))  # Извлекаем ID транзакции на основе выбранного индекса

        date = self.ui_window.date_choosing.text()
        category = self.ui_window.choosing_category.currentText()
        description = self.ui_window.description_edit.text()
        balance = self.ui_window.sum_edit.text()
        status = self.ui_window.increase_decrease.currentText()
        # Получаем нужные нам данные (дата, категория, описание, сумму и статус)

        self.conn.update_transaction_request(date, category, description, balance, status, id)
        # Обновляем транзакцию в базе данных с использованием полученных данных

        self.new_transaction.close()  # Закрываем окно создания/редактирования транзакции

    def delete_current_transaction(self):
        index = self.ui.transactions_table.selectedIndexes()[0]
        id = str(self.ui.transactions_table.model().data(index))

        self.conn.delete_transaction_request(id)  # Удаляем транзакцию из базы данных по её ID





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenceTracker()
    window.show()

    sys.exit(app.exec())
