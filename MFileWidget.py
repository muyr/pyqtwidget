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
import os
from MTool import *
'''
Class Name: MFileWidget
Type      : QWidget

 +--------------------+ +------+ +--------+ +------+
 |                    | | file | | Folder | | view |
 +--------------------+ +------+ +--------+ +------+

Public Method:
    void    clear()
    void    setDialogTitle(QString)
    void    setFileFilter(QString)
    QString text()
    void    setText(QString)

Public Slot:
    void    slotClear(bool)
'''


class MFileWidget(QWidget):
    def __init__(self, title = 'File', fileFilter = 'All Files(*)', parent = None):
        super(MFileWidget, self).__init__(parent)
        self.dialogTitle = title
        self.fileFilter = fileFilter

        self.lineEdit = QLineEdit('')

        fileButton = QToolButton()
        fileButton.setToolTip(self.tr('Spec File'))
        fileButton.setAutoRaise(True)
        fileButton.setIcon(QIcon('./images/open.png'))

        viewDirButton = QToolButton()
        viewDirButton.setToolTip(self.tr('Open Dir'))
        viewDirButton.setAutoRaise(True)
        viewDirButton.setIcon(QIcon('./images/opendir.png'))

        viewFileButton = QToolButton()
        viewFileButton.setToolTip(self.tr('View File'))
        viewFileButton.setAutoRaise(True)
        viewFileButton.setIcon(QIcon('./images/openfile.png'))

        self.connect(fileButton, SIGNAL('clicked()'), self.slotOpenDialog)
        self.connect(viewDirButton, SIGNAL('clicked()'), self.slotViewDir)
        self.connect(viewFileButton, SIGNAL('clicked()'), self.slotViewFile)
        self.connect(self.lineEdit, SIGNAL('returnPressed()'), self.slotTextChanged)

        mainLay = QHBoxLayout()
        mainLay.addWidget(self.lineEdit)
        mainLay.addWidget(fileButton)
        mainLay.addWidget(viewDirButton)
        mainLay.addWidget(viewFileButton)
        mainLay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLay)

    def slotOpenDialog(self):
        file = QFileDialog.getOpenFileName(self, self.dialogTitle, '', self.fileFilter)
        # PySide return tuple, ([], '')
        # PyQt   return list,  []
        if isinstance(file, tuple): file = file[0]
        if file != '':
            self.setText(file)

    def slotTextChanged(self):
        if not os.path.isfile(self.text()):
            QMessageBox.warning(self, 'Warning', 'File doesn\'t exist!')

    def slotViewFile(self):
        openFile(self.text())

    def slotViewDir(self):
        openDir(self.text())

    def setDialogTitle(self, title):
        self.dialogTitle = title

    def setFileFilter(self, filter):
        self.fileFilter = filter

    def slotClear(self, flag):
        self.lineEdit.setText('')

    def text(self):
        return self.lineEdit.text()

    def setText(self, text):
        self.lineEdit.setText(text)