# This Python file uses the following encoding: utf-8
#model_view_ex.py
import sys, csv
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTableView,
    QVBoxLayout
)
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class DisplayParts(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle("Model and View Example")

        self.setupModelView()

        self.show()

    def setupModelView(self):
        """
        Set up standard item model and table view.
        """
        self.model = QStandardItemModel()

        table_view = QTableView()
        # From QAbstractItemView.ExtendedSelection = 3
        table_view.SelectionMode(3)
        table_view.setModel(self.model)

        # Set initial row and column values
        self.model.setRowCount(3)
        self.model.setColumnCount(4)

        self.loadCSVFile()

        v_box = QVBoxLayout()
        v_box.addWidget(table_view)

        self.setLayout(v_box)

    def loadCSVFile(self):
        """
        Load header and rows from CSV file.
        Items are constructed before adding them to the table.
        """
        file_name = "files/parts.csv"

        with open(file_name, "r") as csv_f:
            reader = csv.reader(csv_f)
            header_labels = next(reader)
            self.model.setHorizontalHeaderLabels(header_labels)
            for i, row in enumerate(csv.reader(csv_f)):
                items = [QStandardItem(item) for item in row]
                self.model.insertRow(i, items)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DisplayParts()
    sys.exit(app.exec_())
