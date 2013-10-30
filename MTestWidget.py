# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.08
# Email : muyanru345@163.com
###################################################################
from MPyQtWidget_test import *
import os

classDict = {
            'MListWidgetDialog':MListWidgetDialogTest,
            'MSeparator':MSeparatorTest,
            'MTextEditDialog':MTextEditDialogTest,
            'MFolderWidget':MFolderWidgetTest,
            'MFileWidget':MFileWidgetTest,
            'MHtmlTextLabel':MHtmlTextLabelTest,
            'MPictureLabel':MPictureLabelTest,
            'MDustbinButton':MDustbinButtonTest,
            'MMultiFileWidget':MMultiFileWidgetTest,
            'MMultiControlWidget':MMultiControlWidgetTest,
            'MMultiTabWidget':MMultiTabWidgetTest,
            'MTMallPicWidget':MTMallPicWidgetTest
            }

class MTestButton(QPushButton):
    def __init__(self, className = QWidget, parent = None):
        super(MTestButton, self).__init__(parent)
        self.connect(self, SIGNAL('clicked()'), self.slotClicked)

    def setClass(self, className):
        self.className = className

    def slotClicked(self):
        dialog = QDialog(self)
        test = self.className()
        lay = QHBoxLayout()
        lay.addWidget(test)
        dialog.setLayout(lay)
        dialog.show()

class MTestWindow(QWidget):
    def __init__(self, parent = None):
        super(MTestWindow, self).__init__(parent)
        self.setWindowTitle('Test pyqtwidget')
        self.initUI()

    def initUI(self):
        mainLay = QVBoxLayout()
        for classN in classDict.keys():
            tempButton = MTestButton()
            tempButton.setText(classN)
            tempButton.setClass(classDict.get(classN))
            mainLay.addWidget(tempButton)

        self.setLayout(mainLay)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MTestWindow()
    test.show()
    sys.exit(app.exec_())
