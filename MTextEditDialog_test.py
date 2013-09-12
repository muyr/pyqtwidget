# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import sys
from MTextEditDialog import *

''' Test
Public Method:
    void setTextContent(QString)
    void setDialogTitle(QString)
    void setLabel(QString)

Public Signal:
    sigDocumentModifed(QString)
'''

class MTextEditDialogTest(QWidget):
    def __init__(self, parent = None):
        super(MTextEditDialogTest, self).__init__(parent)
        self.setWindowTitle('Test - MTextEditDialog')
        self.initUI()

    def initUI(self):
        content = '''############################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
############################'''
        self.textEdit = QTextEdit('')
        self.textEdit.setDocument(QTextDocument(content))
        self.textEdit.setReadOnly(True)
        butTextEditDialog = QPushButton('MTextEditDialog')
        self.connect(butTextEditDialog, SIGNAL('clicked()'), self.slotShowTextEditDialog)

        mainLay = QVBoxLayout()
        mainLay.addWidget(butTextEditDialog)
        mainLay.addWidget(self.textEdit)

        self.setLayout(mainLay)

    def slotShowTextEditDialog(self):
        dialog = MTextEditDialog()
        # method 3/3
        dialog.setTextContent(self.textEdit.document().toPlainText())
        dialog.setDialogTitle('Modify')
        dialog.setLabel('Information:')
        # signal 1/1
        self.connect(dialog, SIGNAL('sigDocumentModifed(QString)'), self.slotChangeTextEditContent)
        dialog.exec_()

    def slotChangeTextEditContent(self, content):
        self.textEdit.setDocument(QTextDocument(content))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MTextEditDialogTest()
    test.show()
    sys.exit(app.exec_())




