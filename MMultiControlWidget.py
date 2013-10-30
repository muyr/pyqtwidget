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

'''
Class Name: MMultiControlWidget
Type      : QWidget

+------------------------------------------+
| +--------+ +-----+ +---+ +---+ +-------+ |
| | Label: | |   3 | | + | | - | | Clear | |
| +--------+ +-----+ +---+ +---+ +-------+ |
+------------------------------------------+

Public Method:
    void setLabel(QString)
    void setCount(int)
    int  count()

Public Signal:
    void sigAdd()
    void sigRemove()
    void sigCleanAll()
'''

class MMultiControlWidget(QWidget):
    def __init__(self, name = 'Default Number:', parent = None):
        super(MMultiControlWidget, self).__init__(parent)

        self.numLab = QLabel(name)

        self.numLineEdit = QLineEdit('0')
        self.numLineEdit.setReadOnly(True)
        self.numLineEdit.setFixedSize(40, 24)
        self.connect(self.numLineEdit, SIGNAL('textChanged(QString)'), self.slotChangeNum)

        self.addButton = QToolButton()
        self.addButton.setIcon(QIcon('./images/add.png'))
        self.addButton.setIconSize(QSize(20, 20))
        self.addButton.setFixedSize(24, 24)

        self.removeButton = QToolButton()
        self.removeButton.setIcon(QIcon('./images/remove.png'))
        self.removeButton.setIconSize(QSize(20, 20))
        self.removeButton.setFixedSize(24, 24)
        self.removeButton.setEnabled(False)

        self.cleanAllButton = QPushButton('Clear All')
        self.cleanAllButton.setFixedSize(80, 24)
        self.cleanAllButton.setEnabled(False)

        self.connect(self.addButton, SIGNAL('clicked()'), self.slotAdd)
        self.connect(self.removeButton, SIGNAL('clicked()'), self.slotRemove)
        self.connect(self.cleanAllButton, SIGNAL('clicked()'), self.slotClean)

        mainLay = QHBoxLayout()
        mainLay.setSpacing(1)
        mainLay.setContentsMargins(0, 0, 0, 0)

        mainLay.addWidget(self.numLab)
        mainLay.addWidget(self.numLineEdit)
        mainLay.addWidget(self.addButton)
        mainLay.addWidget(self.removeButton)
        mainLay.addWidget(self.cleanAllButton)
        mainLay.addStretch()

        self.setLayout(mainLay)

    def setLabel(self, text):
        self.numLab.setText(text)

    def count(self):
        return int(self.numLineEdit.text())

    def setCount(self, count):
        self.numLineEdit.setText(str(count))

    def slotDecrease(self):
        self.setCount(self.count() - 1)

    def slotIncrease(self):
        self.setCount(self.count() + 1)

    def slotAdd(self):
        self.slotIncrease()
        self.emit(SIGNAL('sigAdd()'))

    def slotRemove(self):
        self.slotDecrease()
        self.emit(SIGNAL('sigRemove()'))

    def slotClean(self):
        self.setCount(0)
        self.emit(SIGNAL('sigCleanAll()'))

    def slotChangeNum(self, text):
        newNum = int(text)
        if newNum < 1:
            self.removeButton.setEnabled(False)
            self.cleanAllButton.setEnabled(False)
        else:
            self.removeButton.setEnabled(True)
            self.cleanAllButton.setEnabled(True)
        if newNum >= 20 :
            self.addButton.setEnabled(False)
        else:
            self.addButton.setEnabled(True)
