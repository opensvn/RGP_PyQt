#!/usr/bin/env python

from __future__ import division
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineEdit = QlineEdit("Type an expression and press Enter")
        self.lineEdit.selectAll()

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        
        self.lineEdit.setFocus()
        self.connect(self.lineEdit, SIGNAL("returnPressed()"),
                self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = unicode(self.lineEdit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append(
                    "<font color=red>%s is invalid!</font>" % text)

def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
