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

        lay1 = QHBoxLayout()
        lay1.addWidget(labelSepH)
        lay1.addWidget(MVSeparator())
        lay1.addWidget(labelSepV)


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

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay3)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(lay4)

        self.setLayout(mainLay)

    def slotClickHtmlTextLabel(self, link):
        if os.path.isfile(link) or os.path.isdir(link):
            os.startfile(link)

    def slotDustbinClicked(self, data):
        self.htmlTextLab.setLabelText(self.htmlTextLab.getLabelText() + str(data))

