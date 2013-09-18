# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import sys
from MSeparator import *

'''
Test:
Class
    MHSeparator
    MVSeparator
'''

class MSeparatorTest(QWidget):
    def __init__(self, parent = None):
        super(MSeparatorTest, self).__init__(parent)
        self.setWindowTitle('Test - MSeparator')
        self.initUI()

    def initUI(self):
        # MHSperator  MVSeparator
        labelSepH = QLabel('MHSeparator:')
        labelSepV = QLabel('<-- MVSeparator')

        lay1 = QHBoxLayout()
        lay1.addWidget(labelSepH)
        lay1.addWidget(MVSeparator())
        lay1.addWidget(labelSepV)

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(MHSeparator())

        self.setLayout(mainLay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MSeparatorTest()
    test.show()
    sys.exit(app.exec_())