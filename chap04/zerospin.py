#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ZeroSpinBox(QSpinBox):
    zeros = 0

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)
        self.connect(self, SIGNAL("valueChanged(int)"),
            self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero"), self.zeros)

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        zerospinbox = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(zerospinbox)
        self.setLayout(layout)

        self.connect(zerospinbox, SIGNAL("atzero"), self.announce)

        self.setWindowTitle("ZeroSpinBox")

    def announce(self, zeros):
        print "ZeroSpinBox has been at zero %d times" % zeros

def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
