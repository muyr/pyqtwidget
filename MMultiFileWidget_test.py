# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import os,sys
from MMultiFileWidget import *

''' Test
Public Method:
    void        setDialogTitle(QString)
    void        setFileFilter(QString)
    void        setGroupTitle(QString)
    QStringList getFileList()

Public Signal:
    void        sigFileListChanged(QStringList)
'''

class MMultiFileWidgetTest(QWidget):
    def __init__(self, parent = None):
        super(MMultiFileWidgetTest, self).__init__(parent)
        self.setWindowTitle('Test - MMultiFileWidget')
        self.initUI()

    def initUI(self):
        # MMultiFileWidget
        self.multiFileWidget = MMultiFileWidget()

        # method 3/4
        self.multiFileWidget.setDialogTitle('Test Dialog Title')
        self.multiFileWidget.setFileFilter('Images(*.png *.jpg *.bmp);;All Files(*)')
        self.multiFileWidget.setGroupTitle('Group Title')

        # signal 1/1
        self.connect(self.multiFileWidget, SIGNAL('sigFileListChanged(QStringList)'), self.slotFileListChanged)

        self.multiTextEdit = QTextEdit()
        self.multiTextEdit.setReadOnly(True)
        getFileListButton = QPushButton('Get File List')
        self.connect(getFileListButton, SIGNAL('clicked()'), self.slotGetFileList)
        self.getFileListTextEdit = QTextEdit()
        self.getFileListTextEdit.setReadOnly(True)

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.multiFileWidget)
        mainLay.addWidget(self.multiTextEdit)
        mainLay.addWidget(getFileListButton)
        mainLay.addWidget(self.getFileListTextEdit)

        self.setLayout(mainLay)

    def slotFileListChanged(self, fileList):
        content = '\n'.join(fileList)
        self.multiTextEdit.setDocument(QTextDocument(content))

    def slotGetFileList(self):
        # method 4/4
        fielList = self.multiFileWidget.getFileList()
        content = '\n'.join(fielList)
        self.getFileListTextEdit.setDocument(QTextDocument(content))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MMultiFileWidgetTest()
    test.show()
    sys.exit(app.exec_())