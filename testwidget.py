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

        # MHtmlTextLabel
        self.htmlTextLab = MHtmlTextLabel()
        self.htmlTextLab.setLink('.')
        self.htmlTextLab.setLabelText('Go To Current Dir')
        self.htmlTextLab.setColor1('#ff0000')
        self.htmlTextLab.setColor2('#00ff00')
        self.htmlTextLab.setFontSize('13pt')
        self.connect(self.htmlTextLab, SIGNAL('sigClicked(QString)'), self.slotClickHtmlTextLabel)


        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(MHSeparator())
        mainLay.addWidget(self.htmlTextLab)

        self.setLayout(mainLay)

    def slotClickHtmlTextLabel(self, link):
        if os.path.isfile(link) or os.path.isdir(link):
            os.startfile(link)

