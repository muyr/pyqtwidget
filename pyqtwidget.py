# -*- coding: cp936 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.08
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

QTextCodec.setCodecForTr(QTextCodec.codecForName("gbk"))

class MHSeparator(QFrame):
    def __init__(self, parent = None):
        super(MHSeparator, self).__init__(parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

class MVSeparator(QFrame):
    def __init__(self, parent = None):
        super(MVSeparator, self).__init__(parent)
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Plain)

class MListWidgetDialog(QDialog):
    def __init__(self, itemList, parent = None):
        super(MListWidgetDialog, self).__init__(parent)
        self.setWindowTitle(self.tr('Double Click To Choose'))

        self.listWidget = QListWidget()
        for item in itemList:
            self.listWidget.addItem(self.tr(item))
        self.connect(self.listWidget, SIGNAL('itemDoubleClicked(QListWidgetItem*)'), self.slotDoubleClicked)

        okButton = QPushButton(self.tr('OK'))
        cancelButton = QPushButton(self.tr('Cancel'))
        okButton.setFixedHeight(30)
        cancelButton.setFixedHeight(30)
        self.connect(okButton, SIGNAL('clicked()'), self.slotOK)
        self.connect(cancelButton, SIGNAL('clicked()'), self.close)

        butLay = QHBoxLayout()
        butLay.addWidget(okButton)
        butLay.addWidget(cancelButton)

        mainLay = QVBoxLayout()
        mainLay.addWidget(self.listWidget)
        mainLay.addLayout(butLay)
        self.setLayout(mainLay)

    def setSingleSelectionMode(self):
        self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)

    def setMultiSelectionMode(self):
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def slotDoubleClicked(self, item):
        self.emit(SIGNAL('selectedItemTextList(QStringList)'), [item.text(), ])
        self.close()

    def slotOK(self):
        itemList = self.listWidget.selectedItems()
        if itemList:
            itemTestList = []
            for item in itemList:
                itemTestList.append(item.text())
            self.emit(SIGNAL('selectedItemTextList(QStringList)'), itemTestList)
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Please select one item at least!')