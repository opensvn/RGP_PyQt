#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        spinBox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinBox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"),
            spinBox.setValue)
        self.connect(spinBox, SIGNAL("valueChanged(int)"),
            dial.setValue)

        # self.connect(dial, SIGNAL("valueChanged(int)"),
        #     spinbox, SLOT("setValue(int)"))
        # self.connect(spinbox, SIGNAL("valueChanged(int)"),
        #     dial, SLOT("setValue(int)"))

        self.setWindowTitle("Signals and Slots")
        
def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()