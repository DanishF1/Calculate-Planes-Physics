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

class MainCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculate Plane Physics")
        self.setGeometry(980, 540, 500, 600)

        #COLUMN 1
        self.t1 = QLabel("Sweep Angle [θ]:")
        self.sweepAngle = QLineEdit()

        self.t2 = QLabel("Wings Area [m²]:")
        self.wingsArea = QLineEdit()

        self.t3 = QLabel("Weight [kg]:")
        self.weight = QLineEdit()

        self.t4 = QLabel("Wings Length: [m]")
        self.wingsLength = QLineEdit()

        self.t5 = QLabel("Tip Length [m]:")
        self.tipLength = QLineEdit()

        self.t6 = QLabel("Weight [m]:")
        self.rootChord = QLineEdit()

        self.calculate = QPushButton("Calculate")
        self.calculate.clicked.connect(self.calculateNow)

        #COLUMN 2
        self.editText = QTextEdit()
        self.editText.setReadOnly(True)

        self.master = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()

        self.col1.addWidget(self.t1)
        self.col1.addWidget(self.sweepAngle)
        self.col1.addWidget(self.t2)
        self.col1.addWidget(self.wingsArea)
        self.col1.addWidget(self.t3)
        self.col1.addWidget(self.wingsLength)
        self.col1.addWidget(self.t4)
        self.col1.addWidget(self.tipLength)
        self.col1.addWidget(self.t5)
        self.col1.addWidget(self.rootChord)
        self.col1.addWidget(self.t6)
        self.col1.addWidget(self.weight)
        self.col1.addWidget(self.calculate)

        self.col2.addWidget(self.editText)
        self.master.addLayout(self.col1, 45)
        self.master.addLayout(self.col2, 55)

        self.col1.setSpacing(0)
        self.setLayout(self.master)

    def calculateNow(self):
        CalculatePlane()


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
    # Run it down
    app = QApplication(sys.argv)
    window = MainCalc()
    window.show()
    sys.exit(app.exec_())




