# -*- coding: cp936 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.08
# Email : muyanru345@163.com
###################################################################
from pyqtwidget import *

class MTestWindow(QWidget):
    def __init__(self, parent = None):
        super(MTestWindow, self).__init__(parent)
        self.setWindowTitle('Test pyqtwidget')
        labelSepH = QLabel('MHSeparator:')
        labelSepV = QLabel('<-- MVSeparator')
        self.butMListWidgetDialog = QPushButton('MListWidgetDialog')
        self.connect(self.butMListWidgetDialog, SIGNAL('clicked()'), self.slotShowListWidgetDialog)

        lay1 = QHBoxLayout()
        lay1.addWidget(labelSepH)
        lay1.addWidget(MVSeparator())
        lay1.addWidget(labelSepV)
        lay1.addWidget(MVSeparator())
        lay1.addWidget(self.butMListWidgetDialog)

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(MHSeparator())

        self.setLayout(mainLay)

    def slotShowListWidgetDialog(self):
        testList = ['Tom', 'Jim', 'Tim', 'Lily', 'Lucy']
        dialog = MListWidgetDialog(testList, self)
        dialog.setMultiSelectionMode()
        self.connect(dialog, SIGNAL('selectedItemTextList(QStringList)'), self.slotChangeButtonText)
        dialog.exec_()

    def slotChangeButtonText(self, testList):
        content = ''
        for i in range(len(testList)):
            if not i: content = testList[i] 
            else: content = content + ',' + testList[i]

        self.butMListWidgetDialog.setText(content)