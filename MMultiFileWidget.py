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

from MDustbinButton import *
from MFileWidget import *

'''
Class Name: MMultiFileWidget
Type      : QWidget

+--GroupTitle-----------------------------------+
|       +----------------------+ +------------+ |
|       |   Add(Multi)...      | |  Clear All | |
|       +----------------------+ +------------+ |
| +---+ +--------------+ +----+ +------+ +----+ |
| | D | |c:/aaa/a.png  | |file| |Folder| |view| |
| +---+ +--------------+ +----+ +------+ +----+ |
| +---+ +--------------+ +----+ +------+ +----+ |
| | D | |c:/aaa/b.png  | |file| |Folder| |view| |
| +---+ +--------------+ +----+ +------+ +----+ |
| +---+ +--------------+ +----+ +------+ +----+ |
| | D | |c:/aaa/c.png  | |file| |Folder| |view| |
| +---+ +--------------+ +----+ +------+ +----+ |
+-----------------------------------------------+

Public Method:
    void        setDialogTitle(QString)
    void        setFileFilter(QString)
    void        setGroupTitle(QString)
    QStringList getFileList()

Public Signal:
    void        sigFileListChanged(QStringList)
'''


class MMultiFileWidget(QWidget):
    def __init__(self, parent = None):
        super(MMultiFileWidget, self).__init__(parent)

        self.dataDict = {}
        self.dialogTitle = ('渲染效果图:').decode('gbk')
        self.fileFilter = 'Image File(*.png *.jpg *.jpeg *.bmp)'

        self.addPictureButton = QPushButton(('添加（可一次选中多个）...').decode('gbk'))
        self.addPictureButton.setFixedHeight(30)
        self.connect(self.addPictureButton, SIGNAL('clicked()'), self.slotAddPic)

        self.removeAllButton = QPushButton(('清除所有').decode('gbk'))
        self.removeAllButton.setFixedWidth(100)
        self.removeAllButton.setFixedHeight(30)
        self.removeAllButton.setEnabled(False)
        self.connect(self.removeAllButton, SIGNAL('clicked()'), self.slotCleanAll)

        buttLay = QHBoxLayout()
        buttLay.addWidget(self.addPictureButton)
        buttLay.addWidget(self.removeAllButton)

        self.previewLay = QGridLayout()
        self.previewLay.addLayout(buttLay, 0, 1)

        self.basicGrpBox = QGroupBox()
        self.basicGrpBox.setTitle('MMultiFileWidget')
        self.basicGrpBox.setLayout(self.previewLay)

        mainLay = QVBoxLayout()
        mainLay.setContentsMargins(0, 0, 0, 0)
        mainLay.addWidget(self.basicGrpBox)
        self.setLayout(mainLay)

    def slotAddPic(self):
        fileList = QFileDialog.getOpenFileNames(self, self.dialogTitle, '', self.fileFilter)
        # PySide return tuple, ([], '')
        # PyQt   return list,  []
        if isinstance(fileList, tuple): fileList = fileList[0]
        if len(fileList):
            for i in fileList:
                self.addWidget(i)
        self.emit(SIGNAL('sigFileListChanged(QStringList)'), self.getFileList())

    def addWidget(self, file):
        row = self.previewLay.rowCount()
        previewWidget = MFileWidget()
        previewWidget.setText(file)
        dustbinButt = MDustbinButton(row)
        dustbinButt.setSize(25)
        self.connect(dustbinButt, SIGNAL('sigClicked(int)'), self.slotRemoveOne)

        self.previewLay.addWidget(dustbinButt, row, 0)
        self.previewLay.addWidget(previewWidget, row, 1)
        self.dataDict[row] = (previewWidget, dustbinButt)
        self.removeAllButton.setEnabled(True)


    def slotCleanAll(self):
        items = self.dataDict.values()
        for item in items :
            item[0].setVisible(False)
            item[1].setVisible(False)
            self.previewLay.removeWidget(item[0])
            self.previewLay.removeWidget(item[1])
        self.dataDict.clear()
        self.removeAllButton.setEnabled(False)
        self.emit(SIGNAL('sigFileListChanged(QStringList)'), self.getFileList())

    def slotRemoveOne(self, state):
        items = self.dataDict.pop(state)
        items[0].setVisible(False)
        items[1].setVisible(False)
        self.previewLay.removeWidget(items[0])
        self.previewLay.removeWidget(items[1])
        if len(self.dataDict.keys()) == 0: 
            self.removeAllButton.setEnabled(False)
        self.emit(SIGNAL('sigFileListChanged(QStringList)'), self.getFileList())

    def getFileList(self):
        resultList = []
        for i in self.dataDict.keys():
            tx = self.dataDict[i][0].text()
            if tx != '': resultList.append(tx)
        return resultList

    def setDialogTitle(self, title):
        self.dialogTitle = title

    def setFileFilter(self, filter):
        self.fileFilter = filter

    def setGroupTitle(self, text):
        self.basicGrpBox.setTitle(text)
