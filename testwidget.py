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
        # MHSperator  MVSeparator and MListWidgetDialog
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

        #  MTextEditDialog
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

        # MFolderWidget
        folderLab = QLabel('FolderWidget:')
        folderWidget = MFolderWidget()
        folderWidget.setDialogTitle('FolderWidgetTitle')
        butClear = QPushButton('Clear')
        self.connect(butClear, SIGNAL('clicked(bool)'), folderWidget, SLOT('slotClear(bool)'))

        # MFileWidget
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

        # MHtmlTextLabel
        self.htmlTextLab = MHtmlTextLabel()
        self.htmlTextLab.setLink('.')
        self.htmlTextLab.setLabelText('Go To Current Dir')
        self.htmlTextLab.setColor1('#ff0000')
        self.htmlTextLab.setColor2('#00ff00')
        self.htmlTextLab.setFontSize('13pt')
        self.connect(self.htmlTextLab, SIGNAL('sigClicked(QString)'), self.slotClickHtmlTextLabel)

        # MDustbinButton
        dustbinBut = MDustbinButton(5)
        dustbinBut.setSize(30)
        self.connect(dustbinBut, SIGNAL('sigClicked(int)'), self.slotDustbinClicked)
        lay4 = QHBoxLayout()
        lay4.addWidget(self.htmlTextLab)
        lay4.addWidget(dustbinBut)

        # MPictureLabel
        picLabel = MPictureLabel()
        picLabel.setSize(120)
        picLabel.setPicturePath('./images/key.png')
        picLabel.setLink('./images/key.png')
        picLabel.setBorderWidth(2)
        picLabel.setBorderColor('#ff0000')
        self.connect(picLabel, SIGNAL('sigClicked(QString)'), self.slotClickPictureLabel)

        # MMultiFileWidget
        self.multiFileWidget = MMultiFileWidget()
        self.connect(self.multiFileWidget, SIGNAL('sigFileListChanged(QStringList)'), self.slotFileListChanged)
        self.multiTextEdit = QTextEdit()
        self.multiTextEdit.setReadOnly(True)

        lay5 = QVBoxLayout()
        lay5.addWidget(picLabel)
        lay5.addWidget(MHSeparator())
        lay5.addWidget(self.multiFileWidget)
        lay5.addWidget(self.multiTextEdit)

        # MMultiTabWidget
        multiTabWidget = MMultiTabWidget(MMultiFileWidget)
        multiTabWidget.setGroupTitle('Test')

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay2)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay3)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay4)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay5)
        mainLay.addWidget(multiTabWidget)

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

    def slotClickPictureLabel(self, link):
        link  = os.path.abspath(link)
        if os.path.isfile(link) or os.path.isdir(link):
            os.startfile(link)

    def slotDustbinClicked(self, data):
        self.htmlTextLab.setLabelText(self.htmlTextLab.getLabelText() + str(data))

    def slotFileListChanged(self, fileList):
        content = '\n'.join(fileList)
        self.multiTextEdit.setDocument(QTextDocument(content))