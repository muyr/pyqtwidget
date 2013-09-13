# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import os,sys
from MDustbinButton import *

''' Test
Public Method:
    void setSize(int)
    void setData(int)
    int  data()

Public Signal:
    void sigClicked(int)
'''

class MDustbinButtonTest(QWidget):
    def __init__(self, parent = None):
        super(MDustbinButtonTest, self).__init__(parent)
        self.setWindowTitle('Test - MDustbinButton')
        self.initUI()

    def initUI(self):
        dustbinBut = MDustbinButton(5)
        # method 2/3
        dustbinBut.setSize(30)
        dustbinBut.setData(10)
        # signal 1/1
        self.connect(dustbinBut, SIGNAL('sigClicked(int)'), self.slotDustbinClicked)

        self.result = QLabel('')
        # method 1/3
        self.result.setText(str(dustbinBut.data()))
        mainLay = QVBoxLayout()
        mainLay.addWidget(dustbinBut)
        mainLay.addWidget(self.result)

        self.setLayout(mainLay)

    def slotDustbinClicked(self, data):
        self.result.setText(self.result.text() + ' ' + str(data))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MDustbinButtonTest()
    test.show()
    sys.exit(app.exec_())