# -*- coding: cp936 -*-
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

'''
Class Name: MPictureLabel
Type      : QLabel


Public Method:
    void    setLink(QString)
    void    setPicturePath(QString)
    void    setSize(int)
    void    setBorderWidth(int)
    void    setBorderColor(QString)

    QString getLink()
    QString getPicturePath()
    int     getSize()

Public Signal:
    void    sigClicked(QString)
'''


class MPictureLabel(QLabel):
    def __init__(self, link = '', filePath = '', parent = None):
        super(MPictureLabel, self).__init__(parent)
        self.filePath = filePath
        self.link = link
        self.setSize(100)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAlignment(Qt.AlignCenter)
        self.borderWidth = 1
        self.borderColor = '#6a92b8'
        self.setStyleSheet('border-width:' + str(self.borderWidth) + 'px;'
                           + 'border-color:' + self.borderColor + ';'
                           + 'border-style: solid; ')
        self.drawPic()

    def setPicturePath(self, filePath):
        self.filePath = filePath
        self.drawPic()

    def setLink(self, link):
        self.link = link

    def setSize(self, size):
        self.size = size
        self.setFixedSize(self.size, self.size)
        self.drawPic()

    def setBorderWidth(self, width):
        self.borderWidth = width
        self.setStyleSheet('border-width:' + str(self.borderWidth) + 'px;'
                           + 'border-color:' + self.borderColor + ';'
                           + 'border-style: solid; ')

    def setBorderColor(self, color):
        self.borderColor = color
        self.setStyleSheet('border-width:' + str(self.borderWidth) + 'px;'
                           + 'border-color:' + self.borderColor + ';'
                           + 'border-style: solid; ')

    def getSize(self):
        return self.size

    def getLink(self):
        return self.link

    def getPicturePath(self):
        return self.filePath

    def drawPic(self):
        pix = QPixmap(self.filePath)
        w = pix.width()
        h = pix.height()
        if w and h:
            if w > h:
                convertPix = pix.scaledToWidth(self.size, Qt.SmoothTransformation)
            else:
                convertPix = pix.scaledToHeight(self.size, Qt.SmoothTransformation)
            self.setPixmap(convertPix)
        else: 
            self.setPixmap(pix)

    def mousePressEvent(self, event):
        self.emit(SIGNAL('sigClicked(QString)'), self.link)
