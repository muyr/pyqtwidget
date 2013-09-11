# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################

import os,sys
from MTMallPicWidget import *

''' Test
Public Method:
    void    setPicList(QStringList, QStringList)
    void    setItemSize(int)
    void    setMainSize(int)
    void    setBorderWidth(int)
    void    setBorderColor(QString)
Public Signal:
    void    sigMainClicked(QString)
'''

class MTMallPicWidgetTest(QWidget):
    def __init__(self, parent = None):
        super(MTMallPicWidgetTest, self).__init__(parent)
        self.setWindowTitle('Test - MTMallPicWidget')
        self.initUI()

    def initUI(self):
        tmallWidget = MTMallPicWidget()
        # method
        tmallWidget.setPicList(['./images/key.png', './images/dustbin.png'], ['./images/key.png', './images/dustbin.png'])
        tmallWidget.setItemSize(60)
        tmallWidget.setMainSize(300)
        tmallWidget.setBorderWidth(2)
        tmallWidget.setBorderColor('#ff00f0')
        # signal
        self.connect(tmallWidget, SIGNAL('sigMainClicked(QString)'), self.slotMainClicked)

        mainLay = QVBoxLayout()
        mainLay.addWidget(tmallWidget)

        self.setLayout(mainLay)

    def slotMainClicked(self, link):
        link = os.path.abspath(link)
        os.startfile(link)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MTMallPicWidgetTest()
    test.show()
    sys.exit(app.exec_())