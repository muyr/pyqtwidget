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
Class Name: MDustbinButton
Type      : QToolButton

Public Method:
    void setSize(int)
    void setData(int)
    int  data()

Public Signal:
    void sigClicked(int)
'''
class MDustbinButton(QToolButton):
    def __init__(self, data = 0, parent = None):
        super(MDustbinButton, self).__init__(parent)
        self.setData(data)
        self.setToolTip('Remove')
        self.setAutoRaise(True)
        self.setIcon(QIcon('./images/dustbin.png'))
        self.connect(self, SIGNAL('clicked()'), self.slotEmitDelete)

    def slotEmitDelete(self):
        self.emit(SIGNAL('sigClicked(int)'), self.stateData)

    def setData(self, data):
        self.stateData = data

    def data(self):
        return self.stateData

    def setSize(self, w):
        self.setFixedSize(QSize(w, w))
        self.setIconSize(QSize(w-1, w-1))