# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import sys
from MListWidgetDialog import *

''' Test
Public Method:
    void setSingleSelectionMode() # by default
    void setMultiSelectionMode()
    void setDialogTitle(QString)
    void setLabel(QString)

Public Signal:
    sigSelectedItemTextList(QStringList)
'''

class MListWidgetDialogTest(QWidget):
    def __init__(self, parent = None):
        super(MListWidgetDialogTest, self).__init__(parent)
        self.setWindowTitle('Test - MListWidgetDialog')
        self.initUI()

    def initUI(self):
        self.butMListWidgetDialog = QPushButton('MListWidgetDialog')
        self.connect(self.butMListWidgetDialog, SIGNAL('clicked()'), self.slotShowListWidgetDialog)

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.butMListWidgetDialog)

        self.setLayout(mainLay)

    def slotShowListWidgetDialog(self):
        testList = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
        dialog = MListWidgetDialog(testList, self)

        # method 4/4
        dialog.setMultiSelectionMode()
        #dialog.setSingleSelectionMode()
        dialog.setDialogTitle('Work Day')
        dialog.setLabel('Ask for leave:')

        # signal 1/1
        self.connect(dialog, SIGNAL('sigSelectedItemTextList(QStringList)'), self.slotChangeButtonText)
        dialog.exec_()

    def slotChangeButtonText(self, testList):
        content = ''
        for i in range(len(testList)):
            if not i: content = testList[i] 
            else: content = content + ',' + testList[i]

        self.butMListWidgetDialog.setText(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MListWidgetDialogTest()
    test.show()
    sys.exit(app.exec_())