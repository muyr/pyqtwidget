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

from MMultiControlWidget import *

'''
Class Name: MMultiTabWidget
Type      : QWidget

+---GroupTitle-----------------------------+
| +--------+ +-----+ +---+ +---+ +-------+ |
| | Label: | |   3 | | + | | - | | Clear | |
| +--------+ +-----+ +---+ +---+ +-------+ |
| +---++---++---+                    +---+ |
| | 1 || 2 || 3 |                    | x | |
| |   +----------------------------+---+-| |
| |                                      | |
| |          Your Widget                 | |
| |                                      | |
| +--------------------------------------+ |
+------------------------------------------+

Public Method:
    void                setGroupTitle(QString)
    int                 setTemplateWidget(QWidget)
    MMultiControlWidget getControlWidget()
    QWidgetList         getWidgetList()

Public Signal:
    void sigDecrease()
'''

class MMultiTabWidget(QWidget):
    def __init__(self, widget, parent = None):
        super(MMultiTabWidget, self).__init__(parent)
        self.setTemplateWidget(widget)
        self.dataDict = {}

        self.controlWidget = MMultiControlWidget()
        self.connect(self.controlWidget, SIGNAL('sigAdd()'), self.slotAdd)
        self.connect(self.controlWidget, SIGNAL('sigRemove()'), self.slotRemove)
        self.connect(self.controlWidget, SIGNAL('sigCleanAll()'), self.slotCleanAll)
        self.connect(self, SIGNAL('sigDecrease()'), self.controlWidget.slotDecrease)

        self.closeTabButton = QToolButton(self)
        self.closeTabButton.setAutoRaise(True)
        self.closeTabButton.setToolTip(('关闭标签').decode('gbk'))
        self.closeTabButton.setIcon(QIcon('./images/closetab.png'))
        self.connect(self.closeTabButton, SIGNAL('clicked()'), self.slotCloseTab)

        self.tabWidget = QTabWidget()
        self.tabWidget.setCornerWidget(self.closeTabButton, Qt.TopRightCorner)

        widgetLay = QVBoxLayout()
        widgetLay.addWidget(self.controlWidget)
        widgetLay.addWidget(self.tabWidget)
        self.basicGrpBox = QGroupBox()
        self.basicGrpBox.setTitle('MMultiTabWidget')
        self.basicGrpBox.setLayout(widgetLay)

        mainLay = QVBoxLayout()
        mainLay.setContentsMargins(0, 0, 0, 0)
        mainLay.addWidget(self.basicGrpBox)

        self.setLayout(mainLay)
        self.slotAdd()

    def setGroupTitle(self, text):
        self.basicGrpBox.setTitle(text)

    def setTemplateWidget(self, className):
        self.widgetClass = className

    def getControlWidget(self):
        return self.controlWidget

    def slotAdd(self):
        newIndex = self.tabWidget.count() + 1
        templateWidget = self.widgetClass()
        self.tabWidget.addTab(templateWidget, str(newIndex))
        self.dataDict[newIndex] = templateWidget

    def slotRemove(self):
        lastIndex = self.tabWidget.count() - 1
        self.tabWidget.removeTab(lastIndex)
        self.dataDict.pop(lastIndex)

    def slotCleanAll(self):
        self.tabWidget.clear()
        self.dataDict.clear()

    def slotCloseTab(self):
        currentIndex = self.tabWidget.currentIndex()
        self.dataDict.pop(currentIndex + 1)
        self.tabWidget.removeTab(currentIndex)
        # rename
        tempDict = self.dataDict.copy()
        keys = tempDict.keys()
        self.dataDict.clear()
        for i in range(0, self.tabWidget.count()):
            self.tabWidget.setTabText(i, str(i + 1))
            self.dataDict[i + 1] = tempDict.get(keys[i])
        self.emit(SIGNAL('sigDecrease()'))

    def getWidgetList(self):
        resultList = []
        keys = (self.dataDict.keys()).sort()
        for i in keys:
             resultList.append(self.dataDict.get(i))
        return resultList
