# This Python file uses the following encoding: utf-8
# query_examples.py
import sys
from PyQt5.QtSql import QSqlDatabase, QsqlQuery

class QueryExamples:

    def __init__():
        super().__init__()

        self.createConnection()
        self.exampleQueries()

    def createConnection(self):
        """
        Create connection to the database.
        """
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("files/accounts.db")

        if not database.open()
            print("Unable to open data source file.")
            sys.exec(1)  # Error code 1 - signifies error

        def exampleQueries(self):
            """
            Examples of working with the database.
            """
            # Executing a simple query

# if __name__ == "__main__":
#     pass
