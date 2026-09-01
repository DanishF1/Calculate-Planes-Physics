import asyncio
import sys
import PyQt5
from PyQt5 import QtWidgets

import plane
from plane import CalculatePlane
global x
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTextEdit,
    QComboBox,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
    QLineEdit,
    QLabel,
    )
from PyQt5.QtGui import QFont

class Main(QWidget):
    def __init__(self):
        super().__init__()
        ...
    def initUI(self):
        #COLUMN 1
        self.t1 = QLineEdit("Sweep Angle [θ]:")
        self.t1.setReadOnly(True)
        self.sweepAngle = QLineEdit()

        self.t2 = QLineEdit("Wings Area [m²]:")
        self.t2.setReadOnly(True)
        self.wingsArea = QLineEdit()

        self.t3 = QLineEdit("Weight [kg]:")
        self.t3.setReadOnly(True)
        self.weight = QLineEdit()

        self.t4 = QLineEdit("Wings Length: [m]")
        self.t4.setReadOnly(True)
        self.wingsLength = QLineEdit()

        self.t5 = QLineEdit("Tip Length [m]:")
        self.t5.setReadOnly(True)
        self.tipLength = QLineEdit()

        self.t6 = QLineEdit("Weight [m]:")
        self.t6.setReadOnly(True)
        self.rootChord = QLineEdit()

        self.calculate = QPushButton("Calculate")
        self.calculate.clicked.connect(self.calculateNow)



        self.master = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()

        self.col1.addWidget(self.t1)
        self.col1.addWidget(self.sweepAngle)

        def calculateNow(self):
            CalculatePlane().inputData()

class opening():

    def startServices(self):

        x = (input
             (""""What do u want?
             1. Configure plane values
             2. Calculate plane params
             """))
        try:
            valuex = int(x)
        except:
            print("invalid input")
            return opening().startServices()

        if 0<valuex<3:
            match valuex:
                case 1:
                    CalculatePlane().inputData()
                case 2:
                    ...


if __name__ == '__main__':
    # Inisialisasi aplikasi
    app = QApplication(sys.argv)

    # Buat dan tampilkan jendela
    window = SimpleApp()
    window.show()

    # Jalankan event loop
    sys.exit(app.exec_())




