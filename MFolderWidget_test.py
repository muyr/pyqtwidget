# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import os, sys
from MFolderWidget import *

''' Test
Public Method:
    void    setDialogTitle(QString)
    QString text()
    void    setText(QString)
'''

class MFolderWidgetTest(QWidget):
    def __init__(self, parent = None):
        super(MFolderWidgetTest, self).__init__(parent)
        self.setWindowTitle('Test - MFolderWidget')
        self.initUI()

    def initUI(self):
        # MFolderWidget
        self.folderWidget = MFolderWidget()
        # method 2/3
        self.folderWidget.setText(os.path.abspath('.'))
        self.folderWidget.setDialogTitle('FolderWidgetTitle')

        folderLab = QLabel('FolderWidget:')

        lay1 = QHBoxLayout()
        lay1.addWidget(folderLab)
        lay1.addWidget(self.folderWidget)

        button = QPushButton('Get Folder Path')
        self.connect(button, SIGNAL('clicked()'), self.slotClick)
        self.resultLineEdit = QLineEdit('')

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(button)
        mainLay.addWidget(self.resultLineEdit)

        self.setLayout(mainLay)

    def slotClick(self):
        # method 1/3
        self.resultLineEdit.setText(self.folderWidget.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MFolderWidgetTest()
    test.show()
    sys.exit(app.exec_())