# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import os,sys
from MHtmlTextLabel import *

''' Test
Public Method:
    void    setLink(QString)
    void    setLabelText(QString)
    void    setColor1(QString)
    void    setColor2(QString)
    void    setFontSize(QString)
    QString getLink()
    QString getLabelText()

Public Signal:
    void    sigClicked(QString)
'''

class MHtmlTextLabelTest(QWidget):
    def __init__(self, parent = None):
        super(MHtmlTextLabelTest, self).__init__(parent)
        self.setWindowTitle('Test - MHtmlTextLabel')
        self.initUI()

    def initUI(self):
        # MHtmlTextLabel
        self.htmlTextLab = MHtmlTextLabel()
        # method 5/7
        self.htmlTextLab.setLink(os.path.abspath('.'))
        self.htmlTextLab.setLabelText('Go To Current Dir')
        self.htmlTextLab.setColor1('#ff0000')
        self.htmlTextLab.setColor2('#00ff00')
        self.htmlTextLab.setFontSize('13pt')
        # signal 1/1
        self.connect(self.htmlTextLab, SIGNAL('sigClicked(QString)'), self.slotClickHtmlTextLabel)

        resultLay = QGridLayout()
        linkLab = QLabel('link: ')
        # method 1/7
        linkLab2 = QLabel(self.htmlTextLab.getLink())
        textLab = QLabel('labelText: ')
        # method 1/7
        textLab2 = QLabel(self.htmlTextLab.getLabelText())

        resultLay.addWidget(linkLab, 0, 0)
        resultLay.addWidget(linkLab2, 0, 1)
        resultLay.addWidget(textLab, 1, 0)
        resultLay.addWidget(textLab2, 1, 1)

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.htmlTextLab)
        mainLay.addLayout(resultLay)

        self.setLayout(mainLay)

    def slotClickHtmlTextLabel(self, link):
        if os.path.isfile(link) or os.path.isdir(link):
            os.startfile(link)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MHtmlTextLabelTest()
    test.show()
    sys.exit(app.exec_())