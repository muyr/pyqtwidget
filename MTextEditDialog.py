# -*- coding: cp936 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.08
# Email : muyanru345@163.com
###################################################################

try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    import sip
    sip.setapi("QString",  2)
    sip.setapi("QVariant",  2)
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

'''
Class Name: MTextEditDialog
Type      : QDialog
 +-+---------------------+
 |-|    Dialog Title     |
 +-----------------------+
 | Content:              |
 | +-------------------+ |
 | |                   | |
 | |                   | |
 | |                   | |
 | |                   | |
 | |                   | |
 | +-------------------+ |
 +-----------------------+
 | +-------+  +--------+ |
 | |  OK   |  | Cancel | |
 | +-------+  +--------+ |
 +-----------------------+
Public Method:
    void setTextContent(QString)
    void setDialogTitle(QString)
    void setLabel(QString)

Public Signal:
    sigDocumentModifed(QString)
'''

class MTextEditDialog(QDialog):
    def __init__(self, parent = None):
        super(MTextEditDialog, self).__init__(parent)
        self.setWindowTitle('MTextEditDialog')
        self.label = QLabel('Label:')
        self.textEdit = QTextEdit()

        okBut = QPushButton('OK')
        okBut.setFixedHeight(30)
        self.connect(okBut, SIGNAL('clicked()'), self.slotOK)

        cancelBut = QPushButton('Cancel')
        cancelBut.setFixedHeight(30)
        self.connect(cancelBut, SIGNAL('clicked()'), self.close)

        butLay = QHBoxLayout()
        butLay.addWidget(okBut)
        butLay.addWidget(cancelBut)

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.label)
        mainLay.addWidget(self.textEdit)
        mainLay.addLayout(butLay)

        self.setLayout(mainLay)

    def setDialogTitle(self, title):
        self.setWindowTitle(title)

    def setLabel(self, label):
        self.label.setText(label)

    def setTextContent(self, text):
        self.textEdit.setDocument(QTextDocument(text))

    def getTextContent(self):
        return self.textEdit.document().toPlainText()

    def slotOK(self):
        self.emit(SIGNAL('sigDocumentModifed(QString)'), self.getTextContent())
        self.close()