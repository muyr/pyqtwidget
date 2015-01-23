# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2015.1
# Email : muyanru345@163.com
###################################################################


from PySide.QtCore import *
from PySide.QtGui import *


class MShadowWidget(QWidget):
    def __init__(self, parent = None):
        super(MShadowWidget, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)

        self.isLeftPressed = False
        self.currentPosRow = 0
        self.currentPosColumn = 0
        self.centerBackgroudColor = QColor(Qt.white)
        self.scaleMargin = 10

    def setCenterBackgroundColor(self, color):
        self.centerBackgroudColor = color
        self.update()

    def setScaleMargin(self, margin):
        self.scaleMargin = margin

     ######  ##     ## ########   ######   #######  ########  
    ##    ## ##     ## ##     ## ##    ## ##     ## ##     ## 
    ##       ##     ## ##     ## ##       ##     ## ##     ## 
    ##       ##     ## ########   ######  ##     ## ########  
    ##       ##     ## ##   ##         ## ##     ## ##   ##   
    ##    ## ##     ## ##    ##  ##    ## ##     ## ##    ##  
     ######   #######  ##     ##  ######   #######  ##     ## 

    def setCursorType(self, curRow, curColumn):
        if abs(curRow + curColumn) == 2:
            self.setCursor(Qt.SizeFDiagCursor)
        elif abs(curRow) == 1 and (curRow + curColumn) == 0:
            self.setCursor(Qt.SizeBDiagCursor)
        elif abs(curRow + curColumn) == 1 and curRow == 0:
            self.setCursor(Qt.SizeHorCursor)
        elif abs(curRow + curColumn) == 1 and curColumn == 0:
            self.setCursor(Qt.SizeVerCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

    def countColumn(self, point):
        if point.x() < self.scaleMargin:
            return -1
        elif point.x() > self.width() - self.scaleMargin:
            return 1
        else:
            return 0

    def countRow(self, point):
        if point.y() < self.scaleMargin:
            return -1
        elif point.y() > self.height() - self.scaleMargin:
            return 1
        else:
            return 0

    ######## ##     ## ######## ##    ## ######## 
    ##       ##     ## ##       ###   ##    ##    
    ##       ##     ## ##       ####  ##    ##    
    ######   ##     ## ######   ## ## ##    ##    
    ##        ##   ##  ##       ##  ####    ##    
    ##         ## ##   ##       ##   ###    ##    
    ########    ###    ######## ##    ##    ##    

    def mousePressEvent(self, event):
        # 鼠标按下事件
        if event.button() == Qt.LeftButton:
            self.isLeftPressed = True;
            temp = event.globalPos()
            self.lastPos = temp
            self.currentPosRow = self.countRow(event.pos())
            self.currentPosColumn = self.countColumn(event.pos())
            event.ignore()

    def mouseReleaseEvent(self, event):
        # 鼠标释放事件
        if(self.isLeftPressed):
            self.isLeftPressed = False
        QApplication.restoreOverrideCursor()
        event.ignore()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            if windowState() != Qt.WindowFullScreen:
                self.setWindowState(Qt.WindowFullScreen)
            else:
                self.setWindowState(Qt.WindowNoState)
        event.ignore()

    def mouseMoveEvent(self, event):
        if self.isLeftPressed:
            # print self.currentPosRow, self.currentPosColumn
            ptemp = event.globalPos() - self.lastPos
            if self.currentPosRow == 0 and self.currentPosColumn == 0:
                ptemp = ptemp + self.pos()
                self.move(ptemp)
            else:
                windowRect = self.geometry()

                if self.currentPosRow != 0 and self.geometry().height() + ptemp.y() * self.currentPosRow > self.minimumHeight():
                    if self.currentPosRow == -1:
                        windowRect.setTop(windowRect.top() + ptemp.y())
                    elif self.currentPosRow == 1:
                        windowRect.setBottom(windowRect.bottom() + ptemp.y())
                if self.currentPosColumn != 0 and self.geometry().width() + ptemp.x() * self.currentPosColumn > self.minimumWidth(): 
                    if self.currentPosColumn == -1:
                         windowRect.setLeft(windowRect.left() + ptemp.x())
                    elif self.currentPosColumn == 1:
                        windowRect.setRight(windowRect.right() + ptemp.x())
  
                self.setGeometry(windowRect)
                self.updateGeometry()

            self.lastPos = event.globalPos()
            QWidget.mouseMoveEvent(self, event)
            return
        else:
            self.currentPosRow = self.countRow(event.pos())
            self.currentPosColumn = self.countColumn(event.pos())
            self.setCursorType(self.currentPosRow, self.currentPosColumn)
        event.ignore()

    def paintEvent(self, event):
        margin = 5
        roundPix = 3
        backgroudPath = QPainterPath()
        backgroudPath.setFillRule(Qt.WindingFill)
        backgroudPath.addRoundedRect(margin, margin, self.width()-margin*2, self.height()-margin*2, roundPix, roundPix)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        color = QColor(0, 0, 0, 50)
        for i in range(margin):
            shadowPath = QPainterPath()
            shadowPath.setFillRule(Qt.WindingFill)
            shadowPath.addRoundedRect(margin-i, margin-i, self.width()-(margin-i)*2, self.height()-(margin-i)*2, roundPix+2, roundPix+2)
            color.setAlpha(50 - 50*i/margin)
            painter.setPen(color)
            painter.drawPath(shadowPath)

        painter.fillPath(backgroudPath, QBrush(self.centerBackgroudColor))
        painter.end()

 
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    test = MShadowWidget()
    test.show()
    sys.exit(app.exec_())
    