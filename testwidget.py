# -*- coding: cp936 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.08
# Email : muyanru345@163.com
###################################################################
from MPyQtWidget import *
import os

class MTestWindow(QWidget):
    def __init__(self, parent = None):
        super(MTestWindow, self).__init__(parent)
        self.setWindowTitle('Test pyqtwidget')
        self.initUI()

    def initUI(self):
        # MHSperator  MVSeparator and MListWidgetDialog
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

