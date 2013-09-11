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
Class Name: MHtmlTextLabel
Type      : QLabel

+-----------------------------+
|   __H_T_M_L_L_a_b_e_l___    +
+-----------------------------+

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

class MHtmlTextLabel(QLabel):
    def __init__(self, link = '', labelName = 'Label Text', parent = None):
        super(MHtmlTextLabel, self).__init__(parent)
        self.fontSize = '11pt'
        self.color1 = '#ad0e3b'
        self.color2 = '#11aa90'
        self.color = self.color1
        self.setLink(link)
        self.setLabelText(labelName)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.color = self.color2
            self.updateText()
            self.emit(SIGNAL('sigClicked(QString)'), self.link)

    def setLabelText(self, text):
        self.labelName = text
        self.updateText()

    def setLink(self, text):
        #self.setToolTip(text)
        self.link = text

    def getLink(self):
        return self.link

    def getLabelText(self):
        return self.labelName

    def setFontSize(self, size):
        self.fontSize = size
        self.updateText()

    def setColor1(self, text):
        self.color1 = text
        self.updateText()

    def setColor2(self, text):
        self.color2 = text
        self.updateText()

    def updateText(self):
        self.setText('<span style = "color:' + self.color + '; text-decoration: underline; font-size:' + self.fontSize + ';">' 
                      + self.labelName 
                      + '</span>')