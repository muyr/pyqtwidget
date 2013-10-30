# -*- coding: utf-8 -*-
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

'''
Class Name: MListWidgetDialog
Type      : QDialog
 +-+---------------------+
 |-|    Dialog Title     |
 +-----------------------+
 | Label:                |
 | +-------------------+ |
 | |itemList[0]        | |
 | |itemList[1]        | |
 | |itemList[2]        | |
 | |...                | |
 | |itemList[-1]       | |
 | +-------------------+ |
 +-----------------------+
 | +-------+  +--------+ |
 | |  OK   |  | Cancel | |
 | +-------+  +--------+ |
 +-----------------------+
Public Method:
    void setSingleSelectionMode() # by default
    void setMultiSelectionMode()
    void setDialogTitle(QString)
    void setLabel(QString)

Public Signal:
    sigSelectedItemTextList(QStringList)
'''

class MListWidgetDialog(QDialog):
    def __init__(self, itemList, parent = None):
        super(MListWidgetDialog, self).__init__(parent)
        self.setWindowTitle(self.tr('Double Click To Choose'))
        self.label = QLabel('Label:')
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
        mainLay.addWidget(self.label)
        mainLay.addWidget(self.listWidget)
        mainLay.addLayout(butLay)
        self.setLayout(mainLay)

    def setDialogTitle(self, title):
        self.setWindowTitle(title)

    def setLabel(self, label):
        self.label.setText(label)

    def setSingleSelectionMode(self):
        self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)

    def setMultiSelectionMode(self):
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def slotDoubleClicked(self, item):
        self.emit(SIGNAL('sigSelectedItemTextList(QStringList)'), [item.text(), ])
        self.close()

    def slotOK(self):
        itemList = self.listWidget.selectedItems()
        if itemList:
            itemTestList = []
            for item in itemList:
                itemTestList.append(item.text())
            self.emit(SIGNAL('sigSelectedItemTextList(QStringList)'), itemTestList)
            self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'Please select one item at least!')
