# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import os,sys
from MFileWidget import *

''' Test
Public Method:
    void    setDialogTitle(QString)
    void    setFileFilter(QString)
    void    setText(QString)
    QString text()
'''

class MFileWidgetTest(QWidget):
    def __init__(self, parent = None):
        super(MFileWidgetTest, self).__init__(parent)
        self.setWindowTitle('Test - MFileWidget')
        self.initUI()

    def initUI(self):
        # MFileWidget
        self.fileWidget = MFileWidget()
        # method 3/4
        self.fileWidget.setText('./images/open.png')
        self.fileWidget.setDialogTitle('FileWidgetTitle')
        self.fileWidget.setFileFilter('ImageFile(*.png *jpg *bmp *tiff);;All Files(*)')

        fileLab = QLabel('FileWidget:')
        lay1 = QHBoxLayout()
        lay1.addWidget(fileLab)
        lay1.addWidget(self.fileWidget)

        button = QPushButton('Get File Path')
        self.connect(button, SIGNAL('clicked()'), self.slotClick)
        self.resultLineEdit = QLineEdit('')

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(button)
        mainLay.addWidget(self.resultLineEdit)

        self.setLayout(mainLay)

    def slotClick(self):
        # method 1/4
        self.resultLineEdit.setText(self.fileWidget.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MFileWidgetTest()
    test.show()
    sys.exit(app.exec_())