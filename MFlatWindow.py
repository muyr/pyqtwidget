# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2015.1
# Email : muyanru345@163.com
###################################################################

from PySide.QtCore import *
from PySide.QtGui import *
from MShadowWidget import MShadowWidget
import os, sys


class MFlatWindow(MShadowWidget):
    def __init__(self, parent = None):
        super(MFlatWindow, self).__init__(parent)
        self.wrapperBackgroundColor = QColor('#2a2a2a')
        APP_PATH = os.path.realpath(sys.path[0])

        ######## #### ######## ##       ######## 
           ##     ##     ##    ##       ##       
           ##     ##     ##    ##       ##       
           ##     ##     ##    ##       ######   
           ##     ##     ##    ##       ##       
           ##     ##     ##    ##       ##       
           ##    ####    ##    ######## ######## 

        #-------------------< Title >--------------------#
        self.titleIconLab = QLabel()
        self.titleIconLab.setFixedSize(24, 24)
        self.titleIconLab.setScaledContents(True)
        
        self.titleLabel = QLabel()

        self.menuButton = QToolButton()
        self.menuButton.setIcon(QIcon(APP_PATH + '/images/menu.png'))
        self.menuButton.setAutoRaise(True)
        self.menuButton.setIconSize(QSize(24, 24))
        self.connect(self.menuButton, SIGNAL('clicked()'), self.menuButton.showMenu)

        self.minButton = QToolButton()
        self.minButton.setIcon(QIcon(APP_PATH + '/images/min.png'))
        self.minButton.setAutoRaise(True)
        self.minButton.setIconSize(QSize(24, 24))

        self.closeButton = QToolButton()
        self.closeButton.setIcon(QIcon(APP_PATH + '/images/close.png'))
        self.closeButton.setIconSize(QSize(24, 24))
        self.closeButton.setAutoRaise(True)
        self.connect(self.closeButton, SIGNAL('clicked()'), self.close)
        self.connect(self.minButton, SIGNAL('clicked()'), self.showMinimized)
        
        titleLay = QHBoxLayout()
        titleLay.setContentsMargins(5, 0, 0, 0)
        titleLay.setSpacing(0)
        titleLay.addWidget(self.titleIconLab)
        titleLay.addWidget(self.titleLabel)
        titleLay.addStretch()
        titleLay.addWidget(self.menuButton)
        titleLay.addWidget(self.minButton)
        titleLay.addWidget(self.closeButton)

        self.titleWidget = QWidget()
        self.titleWidget.setFixedHeight(30)
        self.titleWidget.setLayout(titleLay)
        self.titleWidget.installEventFilter(self)

        ########   #######  ######## ########  #######  ##     ## 
        ##     ## ##     ##    ##       ##    ##     ## ###   ### 
        ##     ## ##     ##    ##       ##    ##     ## #### #### 
        ########  ##     ##    ##       ##    ##     ## ## ### ## 
        ##     ## ##     ##    ##       ##    ##     ## ##     ## 
        ##     ## ##     ##    ##       ##    ##     ## ##     ## 
        ########   #######     ##       ##     #######  ##     ## 
        
        #-------------------< Bottom >--------------------#
        self.bottomWidget = QWidget()
        self.bottomWidget.setFixedHeight(30)
        self.leftLabel = QLabel()
        self.middleLabel = QLabel()
        self.rightLabel = QLabel()
        bottomLay = QHBoxLayout()
        bottomLay.setContentsMargins(5, 5, 5, 5)
        bottomLay.addWidget(self.leftLabel)
        bottomLay.addStretch()
        bottomLay.addWidget(self.middleLabel)
        bottomLay.addStretch()
        bottomLay.addWidget(self.rightLabel)
        bottomLay.addSpacing(10)
        self.bottomWidget.setLayout(bottomLay)
        self.bottomWidget.installEventFilter(self)

        self.centerLay = QVBoxLayout()
        self.centerLay.setContentsMargins(40, 10, 40, 10)
        mainLay = QVBoxLayout()
        mainLay.setContentsMargins(5, 5, 5, 5)
        mainLay.addWidget(self.titleWidget)
        mainLay.addLayout(self.centerLay)
        mainLay.addStretch()
        mainLay.addWidget(self.bottomWidget)

        self.setLayout(mainLay)
        toolButtonQss = '''
                        QToolButton{background-color:#2a2a2a; 
                                    width:30px;
                                    height:30px;
                                    margin:0px;
                                    padding:0px}
                        QToolButton:hover{background-color:#ee2b2b}
                        QToolButton:pressed{background-color:#ee2b2b}
                        QToolButton:disabled{background-color:#eeeeee}
                        # QToolButton:focus{background-color:#ee2b2b}
                    '''
        self.setTitleButtonQss(toolButtonQss)

    ##      ## ########     ###    ########  ########  ######## ########  
    ##  ##  ## ##     ##   ## ##   ##     ## ##     ## ##       ##     ## 
    ##  ##  ## ##     ##  ##   ##  ##     ## ##     ## ##       ##     ## 
    ##  ##  ## ########  ##     ## ########  ########  ######   ########  
    ##  ##  ## ##   ##   ######### ##        ##        ##       ##   ##   
    ##  ##  ## ##    ##  ##     ## ##        ##        ##       ##    ##  
     ###  ###  ##     ## ##     ## ##        ##        ######## ##     ## 

    def setNoMenu(self, flag):
        self.menuButton.setVisible(not flag)

    def setMTitle(self, text):
        self.titleLabel.setText(text)

    def setMIcon(self, iconPath):
        self.titleIconLab.setPixmap(QPixmap(iconPath))

    def setMMenu(self, contextMenu):
        self.menuButton.setMenu(contextMenu)
        self.connect(self.menuButton, SIGNAL('clicked()'), self.menuButton.showMenu)

    def setRightText(self, text):
        self.rightLabel.setText(text)

    def setMiddleText(self, text):
        self.middleLabel.setText(text)

    def setLeftText(self, text):
        self.leftLabel.setText(text)

    def setTitleHeight(self, height):
        self.titleWidget.setFixedHeight(height)

    def setBottomHeight(self, height):
        self.bottomWidget.setFixedHeight(height)

    def setWrapperBackgroundColor(self, color):
        self.wrapperBackgroundColor = color
        self.update()

    def setWrapperFontQss(self, qss):
        self.titleLabel.setStyleSheet(qss)
        self.leftLabel.setStyleSheet(qss)
        self.middleLabel.setStyleSheet(qss)
        self.rightLabel.setStyleSheet(qss)

    def setTitleButtonQss(self, qss):
        self.menuButton.setStyleSheet(qss)
        self.minButton.setStyleSheet(qss)
        self.closeButton.setStyleSheet(qss)

    def eventFilter(self, object, event):
        if event.type() == QEvent.Paint:
            if object in [self.titleWidget, self.bottomWidget]:
                painter = QPainter(object)
                w = object.width()
                h = object.height()
                backgroudColor = QColor(self.wrapperBackgroundColor)
                brush = QBrush(backgroudColor)
                pen = QPen(backgroudColor)
                painter.setBrush(brush)
                painter.setPen(pen)
                painter.drawRect(object.rect())
                pen2 = QPen()
                pen2.setColor(QColor('#000000'))
                pen2.setWidth(1)
                painter.setPen(pen2)
                if object == self.titleWidget:
                    painter.drawLine (0, h-1, w, h-1)
                elif object == self.bottomWidget:
                    painter.drawLine (0, 0, w, 0)
                painter.end()
        return QFrame.eventFilter(self, object, event)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    test = MFlatWindow()
    test.show()
    sys.exit(app.exec_())
