from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase('QSQLITE')
    connection.setDatabaseName(databaseName)
    if not connection.open():
        QMessageBox.warning(
            None,
            'Contacts Book',
            f'Database Error:{connection.lastError().text()}',
        )
        return False
    _createContactsTable()
    return True

def _createContactsTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec()
