# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import os,sys
from MMultiTabWidget import *

''' Test
Public Method:
    void        setGroupTitle(QString)
    void        setTemplateWidget(QWidget)
    QWidgetList getWidgetList()

Public Signal:
    void sigNumChanged()
'''

class MMultiTabWidgetTest(QWidget):
    def __init__(self, parent = None):
        super(MMultiTabWidgetTest, self).__init__(parent)
        self.setWindowTitle('Test - MMultiTabWidgetTest')
        self.initUI()

    def initUI(self):
        self.multiTabWidget = MMultiTabWidget()
        # method
        self.multiTabWidget.setGroupTitle('Test Group Title')
        self.multiTabWidget.setTemplateWidget(QPushButton)
        # signal
        self.connect(self.multiTabWidget, SIGNAL('sigNumChanged(int)'), self.slotNumChanged)

        self.resultLabel = QLabel('result')

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.multiTabWidget)
        mainLay.addWidget(self.resultLabel)

        self.setLayout(mainLay)

    def slotNumChanged(self, num):
        self.resultLabel.setText('slotNumChanged: ' + str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MMultiTabWidgetTest()
    test.show()
    sys.exit(app.exec_())