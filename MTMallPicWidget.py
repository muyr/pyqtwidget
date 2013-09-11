# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
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

import os
from MPictureLabel import *
from MSeparator import *

'''
Class Name: MTMallPicWidget
Type      : QFrame

+-----------------------------+
| +-------------------------+ |
| |                         | |
| |                         | |
| |                         | |
| |                         | |
| |         Picture         | |
| |                         | |
| |                         | |
| |                         | |
| |                         | |
| |                         | |
| +-------------------------+ |
| +----+ +----+ +----+ +----+ |
| |Pic1| |Pic2| |Pic3| |Pic3| |
| +----+ +----+ +----+ +----+ |
+-------------------------- --+

Public Method:
    void    setPicList(QStringList, QStringList)
    void    setItemSize(int)
    void    setMainSize(int)
    void    setBorderWidth(int)
    void    setBorderColor(QString)
Public Signal:
    void    sigMainClicked(QString)
'''

class MTMallPicWidget(QFrame):
    def __init__(self, linkList = [], filePathList = [], parent = None):
        super(MTMallPicWidget, self).__init__(parent)

        self.setFrameShadow(QFrame.Plain)
        self.setFrameShape(QFrame.Panel)
        defaultWidth = 500
        self.setFixedWidth(defaultWidth + 20)

        self.itemSize = 100

        self.mainView = MPictureLabel()
        self.connect(self.mainView, SIGNAL('sigClicked(QString)'), self, SIGNAL('sigMainClicked(QString)'))
        self.mainView.setSize(defaultWidth)

        self.listGridLayout = QGridLayout()
        self.picLabelList = []
        self.setPicList(linkList, filePathList)

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.mainView)
        mainLay.addWidget(MHSeparator())
        mainLay.addLayout(self.listGridLayout)
        self.setLayout(mainLay)

    def setMainSize(self, width):
        self.setFixedWidth(width + 20)
        self.mainView.setSize(width)
        self.updateGridLayout()

    def setItemSize(self, width):
        self.itemSize = width
        self.updateGridLayout()

    def setBorderWidth(self, width):
        self.mainView.setBorderWidth(width)
        for item in self.picLabelList:
            item.setBorderWidth(width)

    def setBorderColor(self, color):
        self.mainView.setBorderColor(color)
        for item in self.picLabelList:
            item.setBorderColor(color)

    def setPicList(self, linkList, filePathList):
        self.linkList = linkList
        self.filePahtList = filePathList
        self.initMainPicture()
        self.updateGridLayout()

    def initMainPicture(self):
        if len(self.filePahtList):
            self.mainView.setPicturePath(self.filePahtList[0])
            self.mainView.setLink(self.linkList[0])
        else:
            self.mainView.setPicturePath('./images/defaultpic.png')
            self.mainView.setLink('./images/defaultpic.png')

    def updateGridLayout(self):
        w = self.width()
        totalW = 0
        totalNum = int(w / self.itemSize)
        column = 0
        for i in self.picLabelList:
            self.listGridLayout.removeWidget(i)
            i.hide()
        self.picLabelList = []
        for i in range(len(self.filePahtList)):
            item = MPictureLabel(self.linkList[i], self.filePahtList[i]) # link filepath
            self.picLabelList.append(item)
            item.setSize(self.itemSize)
            self.connect(item, SIGNAL('sigClicked(QString)'), self.mainView.setPicturePath)
            self.connect(item, SIGNAL('sigClicked(QString)'), self.mainView.setLink)

            totalW += self.itemSize
            row = int(totalW/w)
            self.listGridLayout.addWidget(item, row, column)
            if column + 1 >= totalNum:
                column = 0
            else: column += 1
