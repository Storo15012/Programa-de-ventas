from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear QTableWidget
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(3)

        # Agregar celdas al QTableWidget
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount() - 1):
                item = QTableWidgetItem('Celda ' + str(i) + str(j))
                self.table.setItem(i, j, item)

            button = QPushButton('Botón ' + str(i))
            code = 'código único ' + str(i)
            button.clicked.connect(lambda checked, code=code: self.buttonClicked(code))
            self.table.setCellWidget(i, self.table.columnCount() - 1, button)

        # Agregar QTableWidget a la ventana principal
        self.setCentralWidget(self.table)

    def buttonClicked(self, code):
        print('Botón con código', code, 'fue presionado')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

