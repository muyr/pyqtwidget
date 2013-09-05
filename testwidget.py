# -*- coding: cp936 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.08
# Email : muyanru345@163.com
###################################################################
from MPyQtWidget import *
import os

class MTestWindow(QWidget):
    def __init__(self, parent = None):
        super(MTestWindow, self).__init__(parent)
        self.setWindowTitle('Test pyqtwidget')
        self.initUI()

    def initUI(self):
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

        folderLab = QLabel('FolderWidget:')
        folderWidget = MFolderWidget()
        folderWidget.setDialogTitle('FolderWidgetTitle')
        butClear = QPushButton('Clear')
        self.connect(butClear, SIGNAL('clicked(bool)'), folderWidget, SLOT('slotClear(bool)'))

        fileLab = QLabel('FileWidget:')
        fileWidget = MFileWidget()
        fileWidget.setDialogTitle('FileWidgetTitle')
        fileWidget.setFileFilter('ImageFile(*.png *jpg *bmp *tiff);;All Files(*)')
        butClear2 = QPushButton('Clear')
        self.connect(butClear2, SIGNAL('clicked(bool)'), fileWidget, SLOT('slotClear(bool)'))
        lay3 = QGridLayout()
        lay3.addWidget(folderLab, 0, 0)
        lay3.addWidget(folderWidget, 0, 1)
        lay3.addWidget(butClear, 0, 2)
        lay3.addWidget(fileLab, 1, 0)
        lay3.addWidget(fileWidget, 1, 1)
        lay3.addWidget(butClear2, 1, 2)

        self.htmlTextLab = MHtmlTextLabel()
        self.htmlTextLab.setLink('.')
        self.htmlTextLab.setLabelText('Go To Current Dir')
        self.htmlTextLab.setColor1('#ff0000')
        self.htmlTextLab.setColor2('#00ff00')
        self.htmlTextLab.setFontSize('13pt')
        self.connect(self.htmlTextLab, SIGNAL('sigClicked(QString)'), self.slotClickHtmlTextLabel)

        dustbinBut = MDustbinButton(5)
        dustbinBut.setSize(30)
        self.connect(dustbinBut, SIGNAL('sigClicked(int)'), self.slotDustbinClicked)
        lay4 = QHBoxLayout()
        lay4.addWidget(self.htmlTextLab)
        lay4.addWidget(dustbinBut)

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay2)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay3)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay4)
        
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

    def slotClickHtmlTextLabel(self, link):
        if os.path.isfile(link) or os.path.isdir(link):
            os.startfile(link)

    def slotDustbinClicked(self, data):
        self.htmlTextLab.setLabelText(self.htmlTextLab.getLabelText() + str(data))