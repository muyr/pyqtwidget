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

        content = '''############################
# Author: Mu yanru
# Date  : 2013.08
# Email : muyanru345@163.com
############################'''
        self.textEdit = QTextEdit('')
        self.textEdit.setDocument(QTextDocument(content))
        self.textEdit.setReadOnly(True)
        butTextEditDialog = QPushButton('Modify')
        self.connect(butTextEditDialog, SIGNAL('clicked()'), self.slotShowTextEditDialog)

        lay2 = QHBoxLayout()
        lay2.addWidget(self.textEdit)
        lay2.addWidget(butTextEditDialog)

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay2)

        self.setLayout(mainLay)

    def slotShowListWidgetDialog(self):
        testList = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
        dialog = MListWidgetDialog(testList, self)
        dialog.setMultiSelectionMode()
        dialog.setDialogTitle('Work Day')
        dialog.setLabel('Ask for leave:')
        self.connect(dialog, SIGNAL('sigSelectedItemTextList(QStringList)'), self.slotChangeButtonText)
        dialog.exec_()

    def slotChangeButtonText(self, testList):
        content = ''
        for i in range(len(testList)):
            if not i: content = testList[i] 
            else: content = content + ',' + testList[i]

        self.butMListWidgetDialog.setText(content)

    def slotShowTextEditDialog(self):
        dialog = MTextEditDialog()
        dialog.setTextContent(self.textEdit.document().toPlainText())
        dialog.setDialogTitle('Modify')
        dialog.setLabel('Information:')
        self.connect(dialog, SIGNAL('sigDocumentModifed(QString)'), self.slotChangeTextEditContent)
        dialog.exec_()

    def slotChangeTextEditContent(self, content):
        self.textEdit.setDocument(QTextDocument(content))