import sys
from pyqtwidget import *

class MTestWindow(QWidget):
    def __init__(self, parent = None):
        super(MTestWindow, self).__init__(parent)
        self.setWindowTitle('Test pyqtwidget')
        labelSepH = QLabel('MHSeparator:')
        sepH = MHSeparator()
        labelSepV = QLabel('<-- MVSeparator')
        sepV = MVSeparator()
        lay1 = QHBoxLayout()
        lay1.addWidget(labelSepH)
        lay1.addWidget(sepV)
        lay1.addWidget(labelSepV)

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(sepH)

        self.setLayout(mainLay)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MTestWindow()
    test.show()
    sys.exit(app.exec_())