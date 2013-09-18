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
Class Name: MFolderWidget
Type      : QWidget

 +--------------------+ +------+ +--------+ 
 |                    | | file | | Folder | 
 +--------------------+ +------+ +--------+ 

Public Method:
    void    setDialogTitle(QString)
    QString text()
    void    setText(QString)
'''

class MFolderWidget(QWidget):
    def __init__(self, parent = None, title = 'Folder'):
        super(MFolderWidget, self).__init__(parent)
        self.dialogTitle = title
        self.lineEdit = QLineEdit('')

        fileButton = QToolButton()
        fileButton.setToolTip(self.tr('Spec Folder'))
        fileButton.setAutoRaise(True)
        fileButton.setIcon(QIcon('./images/open.png'))

        viewFileButton = QToolButton()
        viewFileButton.setToolTip(self.tr('Open Folder'))
        viewFileButton.setAutoRaise(True)
        viewFileButton.setIcon(QIcon('./images/opendir.png'))

        self.connect(fileButton, SIGNAL('clicked()'), self.slotOpenDialog)
        self.connect(viewFileButton, SIGNAL('clicked()'), self.slotViewFile)
        self.connect(self.lineEdit, SIGNAL('returnPressed()'), self.slotTextChanged)

        mainLay = QHBoxLayout()
        mainLay.addWidget(self.lineEdit)
        mainLay.addWidget(fileButton)
        mainLay.addWidget(viewFileButton)
        mainLay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLay)

    def slotOpenDialog(self):
        file = QFileDialog.getExistingDirectory(self, self.dialogTitle)
        if file != '':
            self.lineEdit.setText(file)

    def slotViewFile(self):
        openFile(self.text())

    def slotTextChanged(self):
        if not os.path.isdir(self.text()):
            QMessageBox.warning(self, 'Warning', 'Folder doesn\'t exist!')

    def setDialogTitle(self, title):
        self.dialogTitle = title

    def text(self):
        return self.lineEdit.text()

    def setText(self, text):
        self.lineEdit.setText(text)