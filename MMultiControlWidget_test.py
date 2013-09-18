# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import os, sys
from MMultiControlWidget import *

''' Test
Public Method:
    void setLabel(QString)
    void setCount(int)
    int  count()

Public Signal:
    void sigAdd()
    void sigRemove()
    void sigCleanAll()
'''

class MMultiControlWidgetTest(QWidget):
    def __init__(self, parent = None):
        super(MMultiControlWidgetTest, self).__init__(parent)
        self.setWindowTitle('Test - MMultiControlWidget')
        self.initUI()

    def initUI(self):
        # MMultiControlWidget
        self.controlWidget = MMultiControlWidget()
        # method 2/3
        self.controlWidget.setLabel('Attribute: ')
        self.controlWidget.setCount(2)
        # signal 3/3
        self.connect(self.controlWidget, SIGNAL('sigAdd()'), self.slotAdd)
        self.connect(self.controlWidget, SIGNAL('sigRemove()'), self.slotRemove)
        self.connect(self.controlWidget, SIGNAL('sigCleanAll()'), self.slotCleanAll)

        self.resultLineEdit = QLineEdit('')

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.controlWidget)
        mainLay.addWidget(self.resultLineEdit)

        self.setLayout(mainLay)

    def slotAdd(self):
        # method 1/3
        self.resultLineEdit.setText('Add. Count = ' + str(self.controlWidget.count()))

    def slotRemove(self):
        # method 1/3
        self.resultLineEdit.setText('Remove. Count = ' + str(self.controlWidget.count()))

    def slotCleanAll(self):
        # method 1/3
        self.resultLineEdit.setText('Clean. Count = ' + str(self.controlWidget.count()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MMultiControlWidgetTest()
    test.show()
    sys.exit(app.exec_())