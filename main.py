import sys
from plane import inputData, CalculatePlane
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

#Pure untuk GUI
class MainCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculate Plane Physics")
        self.setGeometry(980, 540, 500, 600)
        self.setStyleSheet("""
                    QWidget {
                        background-color: #333; /* Darker background color */
                        color: #fff; /* Text color */
                    }

                    QPushButton {
                        background-color: #66a3ff; /* Lighter background color for buttons */
                        color: #333; /* Text color for buttons */
                        border: 1px solid #fff; /* White border for buttons */
                        border-radius: 5px; /* Rounded corners for buttons */
                        padding: 5px 10px; /* Padding for buttons */
                    }

                    QPushButton:hover {
                        background-color: #3399ff; /* Lighter background color for buttons on hover */
                    }
                """)

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

        self.sweepAngle.returnPressed.connect(self.clearFocus)
        self.rootChord.returnPressed.connect(self.clearFocus)
        self.weight.returnPressed.connect(self.clearFocus)
        self.tipLength.returnPressed.connect(self.clearFocus)
        self.wingsArea.returnPressed.connect(self.clearFocus)
        self.wingsLength.returnPressed.connect(self.clearFocus)


    def calculateNow(self):
        a = self.sweepAngle.text()
        b = self.weight.text()
        c = self.wingsLength.text()
        d = self.wingsArea.text()
        e = self.rootChord.text()
        f = self.wingsLength.text()
        try:
            if b == "" or c == "" or d == "" or e == "" or f == "":
                self.unselect()
                self.showBlank()
                return self.calculateNow
            elif a == "":
                INPUT = inputData(
                dataSweep = 0.0,
                dataWeight = float(b),
                dataTLength = float(c),
                dataWarea = float(d),
                dataRootChord = float(e),
                dataWlength = float(f))
            else:
                INPUT = inputData(dataSweep=float(a),
                                  dataWeight=float(b),
                                  dataTLength=float(c),
                                  dataWarea=float(d),
                                  dataRootChord=float(e),
                                  dataWlength=float(f))
        except:
            print("err")
            self.unselect()
            self.showError()
            return self.calculateNow

        CalculatePlane.calculatePlane(INPUT)
        self.unselect()
        self.editText.setText(CalculatePlane)

    def unselect(self):
        self.sweepAngle.clear()
        self.wingsArea.clear()
        self.wingsLength.clear()
        self.tipLength.clear()
        self.rootChord.clear()
        self.weight.clear()

    def clearFocus(self):
        self.sweepAngle.clearFocus()
        self.wingsArea.clearFocus()
        self.wingsLength.clearFocus()
        self.tipLength.clearFocus()
        self.rootChord.clearFocus()
        self.weight.clearFocus()

    def showError(self):
        self.editText.setText("Your previous input has error in it, try again")

    def showBlank(self):
        self.editText.setText("Wings Area, Wings Length, Tip Length, Root Chord, or Weight cannot be empty! Try again!")

if __name__ == '__main__':
    # Run it down
    app = QApplication(sys.argv)
    window = MainCalc()
    window.show()
    sys.exit(app.exec_())



