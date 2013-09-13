# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import os,sys
from MPictureLabel import *

''' Test
Public Method:
    void    setLink(QString)
    void    setPicturePath(QString)
    void    setSize(int)
    void    setBorderWidth(int)
    void    setBorderColor(QString)

    QString getLink()
    QString getPicturePath()

Public Signal:
    void    sigClicked(QString)
'''

class MPictureLabelTest(QWidget):
    def __init__(self, parent = None):
        super(MPictureLabelTest, self).__init__(parent)
        self.setWindowTitle('Test - MPictureLabel')
        self.initUI()

    def initUI(self):
        # MPictureLabel
        self.picLabel = MPictureLabel()

        # method 5/7
        self.picLabel.setSize(150)
        self.picLabel.setPicturePath('./images/key.png')
        self.picLabel.setLink('./images/key.png')
        self.picLabel.setBorderWidth(2)
        self.picLabel.setBorderColor('#ff0000')

        # signal 1/1
        self.connect(self.picLabel, SIGNAL('sigClicked(QString)'), self.slotClickPictureLabel)

        getAttrButton = QPushButton('Get Attr')
        self.connect(getAttrButton, SIGNAL('clicked()'), self.slotGetFileList)
        self.getAttrTextEdit = QTextEdit()
        self.getAttrTextEdit.setReadOnly(True)

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.picLabel)
        mainLay.addWidget(getAttrButton)
        mainLay.addWidget(self.getAttrTextEdit)

        self.setLayout(mainLay)

    def slotClickPictureLabel(self, link):
        link  = os.path.abspath(link)
        if os.path.isfile(link) or os.path.isdir(link):
            os.startfile(link)

    def slotGetFileList(self):
        # method 2/7
        link = self.picLabel.getLink()
        picPath = self.picLabel.getPicturePath()

        content = 'link: ' + link + '\npicture path: ' + picPath
        self.getAttrTextEdit.setDocument(QTextDocument(content))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MPictureLabelTest()
    test.show()
    sys.exit(app.exec_())