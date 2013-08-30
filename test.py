# -*- coding: cp936 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.08
# Email : muyanru345@163.com
###################################################################
import sys
from pyqtwidget import *
from testwidget import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MTestWindow()
    test.show()
    sys.exit(app.exec_())