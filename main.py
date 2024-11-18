import sys
import sqlite3

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QTableWidgetItem

from expence_tracker import Ui_MainWindow
from new_transaction import Ui_Dialog


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.conn = sqlite3.connect('expence_db.sqlite')  # Подключение бд

    def add_new_transaction_request(self, date, category, description, balance, status):
        cursor = self.conn.cursor()  # Открываем курсор для работы с бд
        request = 'INSERT INTO expences (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)'
        # Запрос на добавление в таблицу бд expences значений столбцов
        cursor.execute(request, [date, category, description, balance, status])  # Выполнение запроса
        self.conn.commit()  # Фиксирование изменений бд

    def update_transaction_request(self, date, category, description, balance, status, id):
        cursor = self.conn.cursor()
        request = 'UPDATE expences SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?'
        # Запрос на обновление даты, категории, описания, баланса и статуса транзакции по ID.
        cursor.execute(request, [date, category, description, balance, status, id])
        self.conn.commit()

    def delete_transaction_request(self, id):
        cursor = self.conn.cursor()
        request = 'DELETE FROM expences WHERE ID=?'
        # Запрос на удаление транзакции по ID
        cursor.execute(request, [id])
        self.conn.commit()

    def get_total(self, column, filter=None, value=None):
        cursor = self.conn.cursor()
        request = f'SELECT SUM ({column}) FROM expences'
        # Запрос для получения суммы по указанному столбцу
        if filter is not None and value is not None:
            request += f' WHERE {filter} = ?'
        # Условие для фильтрации по статусу, если необходимо

        request_values = []  # Подготавливаем список значений для подстановки в запрос
        if value is not None:  # Добавляем значение фильтрации в список, если оно задано
            request_values.append(value)
        query = cursor.execute(request, request_values)
        # Исполняем запрос с параметрами и получаем результат

        resw = query.fetchone()
        print(resw)
        if resw[0] is None:
            return '0' + '₽'
        if resw:  # Проверяем, есть ли результат для запроса
            return str(resw[0]) + '₽'
        # Возвращаем сумму как строку с символом валюты

        return '0'  # Если нет результата, возвращаем '0'

    def total_balance(self):
        # Метод для получения общего баланса.
        # Вызов метода get_total с указанием столбца 'Balance'
        return self.get_total(column='Balance')

    def total_income(self):
        # Метод для получения общего дохода.
        # Вызов метода get_total, фильтруя по статусу 'Доход' в столбце 'Status'
        return self.get_total(column='Balance', filter='Status', value='Доход')

    def total_outcome(self):
        # Метод для получения общего расхода.
        # Вызов метода get_total, фильтруя по статусу 'Outcome' в столбце 'Status'
        return self.get_total(column='Balance', filter='Status', value='Расход')

    def total_groceries(self):
        return self.get_total(column='Balance', filter='Category', value='Продукты')

    def total_entertainment(self):
        return self.get_total(column='Balance', filter='Category', value='Развлечения')

    def total_pharmacy(self):
        return self.get_total(column='Balance', filter='Category', value='Аптеки')

    def total_other(self):
        return self.get_total(column='Balance', filter='Category', value='Другое')
    # Методы для получения общего расхода по значению категории

    def get_all_table(self):
        cursor = self.conn.cursor()
        request = f'SELECT * FROM expences'
        return cursor.execute(request)
        # Получение данных всей таблицы


class ExpenceTracker(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # super(ExpenceTracker, self).__init__()
        super().__init__()
        self.setupUi(self)
        self.conn = Data()  # Подключение бд

        self.transaction_add.clicked.connect(self.open_new_transaction_window)
        self.transaction_edit.clicked.connect(self.open_new_transaction_window)
        self.transaction_delete.clicked.connect(self.delete_current_transaction)
        # Подключенике методов к соответствующим кнопкам

    def reload_data(self):
        self.balance_sum.setText(self.conn.total_balance())
        self.income_sum.setText(self.conn.total_income())
        self.outcome_sum.setText(self.conn.total_outcome())
        self.groceries_sum.setText(self.conn.total_groceries())
        self.entertainment_sum.setText(self.conn.total_entertainment())
        self.pharmacy_sum.setText(self.conn.total_pharmacy())
        self.other_sum.setText(self.conn.total_other())
        # Отображение сумм на главном экране

    def view_data(self):
        res = self.conn.get_all_table()
        self.transactions_table.setColumnCount(6)
        self.transactions_table.setRowCount(0)
        for i, elem in enumerate(res):
            self.transactions_table.setRowCount(
                self.transactions_table.rowCount() + 1)
            for j, item in enumerate(elem):
                self.transactions_table.setItem(
                    i, j, QTableWidgetItem(str(item)))
        # Заполняем таблицу элементами

    def open_new_transaction_window(self):
        self.new_transaction = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_transaction)
        self.new_transaction.show()  # Открытие окна создания/редактирования транзакции

        if self.sender().text() == 'Добавить транзакцию':
            self.ui_window.pushButton.clicked.connect(self.add_new_transaction)
        elif self.sender().text() == 'Редактировать транзакцию':
            self.ui_window.pushButton.clicked.connect(self.edit_current_transaction)
        # sender().text() определяет надпись на последней нажатой кнопке, и исходя из этого
        # создает новую/меняет старую транзакцию

    def add_new_transaction(self):
        date = self.ui_window.date_choosing.text()
        category = self.ui_window.choosing_category.currentText()
        description = self.ui_window.description_edit.text()
        balance = self.ui_window.sum_edit.text()
        status = self.ui_window.increase_decrease.currentText()
        # Получаем нужные нам данные (дата, категория, описание, сумму и статус)
        if status == 'Income':
            self.conn.add_new_transaction_request(date, category, description, balance, status)
        else:
            self.conn.add_new_transaction_request(date, category, description, '-' + balance, status)
        # Передали в метод, отвечающий за добавление новых данных в бд
        self.view_data()
        self.reload_data()
        self.new_transaction.close()
        # Закрыли окно создания/редактирования транзакции

    def edit_current_transaction(self):
        index = self.transactions_table.selectedIndexes()[0]  # Получаем индекс выбранной транзакции в таблице
        id = int(self.transactions_table.model().data(index))  # Извлекаем ID транзакции на основе выбранного индекса

        date = self.ui_window.date_choosing.text()
        category = self.ui_window.choosing_category.currentText()
        description = self.ui_window.description_edit.text()
        balance = self.ui_window.sum_edit.text()
        status = self.ui_window.increase_decrease.currentText()
        # Получаем нужные нам данные (дата, категория, описание, сумму и статус)

        self.conn.update_transaction_request(date, category, description, balance, status, id)
        # Обновляем транзакцию в базе данных с использованием полученных данных
        self.view_data()
        self.reload_data()
        self.new_transaction.close()  # Закрываем окно создания/редактирования транзакции

    def delete_current_transaction(self):
        index = self.transactions_table.selectedIndexes()[0]
        id = str(self.transactions_table.model().data(index))

        self.conn.delete_transaction_request(id)  # Удаляем транзакцию из базы данных по её ID
        self.view_data()
        self.reload_data()

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.conn.conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenceTracker()
    window.show()

    sys.exit(app.exec())
