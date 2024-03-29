# This Python file uses the following encoding: utf-8
# account_manager.py
import sys, os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QTableView,
    QHeaderView,
    QHBoxLayout,
    QVBoxLayout,
    QSizePolicy,
    QMessageBox
)
from PyQt5.QtSql import (
    QSqlDatabase,
    QSqlQuery,
    QSqlRelationalTableModel,
    QSqlRelation,
    QSqlRelationalDelegate,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class AccountManager(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setMinimumSize(1000, 600)
        self.setWindowTitle("10.1 - Account Management GUI")

        self.createConnection()
        self.createTable()
        self.setupWidgets()

        self.show()

    def createConnection(self):
        database = QSqlDatabase.addDatabase("QSQLITE") # SQLite version 3
        database.setDatabaseName("files/accounts.db")

        if not database.open():
            print("Unable to open data source file.")
            sys.exit(1) # Error code 1 - signifies error

        # Check if the tables we need exist in the database
        tables_needed = {"accounts", "countries"}
        tables_not_found = tables_needed - set(database.tables())
        if tables_not_found:
            QMessageBox.critical(None, "Error", f"The following tables are misiing from the database: {tables_not_found}")
            sys.exit(1) # Error code 1 - signifies error

    def createTable(self):
        """
        Set up the model, headers and populate the model.
        """
        self.model = QSqlRelationTableModel()
        self.model.setTable("accounts")
        self.model.setRelation(self.model.fieldIndex("country_id"), QSqlRelation("countries", "id", "country"))

        self.model.setHeaderData(self.model.fieldIndex("employee_id"), Qt.Horizontal, "Employee ID")
        self.model.setHeaderData(self.model.fieldIndex("first_name"), Qt.Horizontal, "First")

        self.model.setHeaderData(self.model.fieldIndex("last_name"), Qt.Horizontal, "Last")
        self.model.setHeaderData(self.model.fieldIndex("email"), Qt.Horizontal, "E-mail")
        self.model.setHeaderData(self.model.fieldIndex("department"), Qt.Horizontal, "Country")

        # Populate the model with data
        self.model.select()

    def setupWidgets(self):
        """
        Create instances of widgets, the table view and set layouts.
        """
        icons_path = "icons"

        title = QLabel("Account Management System")
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        title.setStyleSheet("font: bold 24px")

        add_record_button = QPushButton("Add Employee")
        add_record_button.setIcon(Icon(os.path.join(icons_path, "add_user.png")))
        add_record_button.setStyleSheet("padding: 10px")
        add_record_button.clicked.connect(self.addRecord)

        del_record_button.setStyleSheet("padding: 10px")
        del_record_button.clicked.connect(self.deleteRecord)

        # Set up sorting combo box
        sorting_options = ["Sort by ID", "Sort by First Name", "Sort by Last Name", "Sort by Department", "Sort by Country"]

        sort_name_cb = QComboBox()
        sort_name_cb.addItems(sorting_options)
        sort_name_cb.currentTextChanged.connect(self.setSortingOrder)

        buttons_h_box = QHBoxLayout()
        buttons_h_box.addWidget(add_record_button)
        buttons_h_box.addWidget(del_record_button)
        buttons_h_box.addStrectch()
        buttons_h_box.addWidget(sort_name_cb)

        # Widget to contain editing buttons
        edit_buttons = QWidget()
        edit_buttons.setLayout(buttons_h_box)

        # Create table view and set model
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



# if __name__ == "__main__":
#     pass
