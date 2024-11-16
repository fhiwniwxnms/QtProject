from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()


    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')