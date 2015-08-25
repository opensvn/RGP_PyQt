#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from functools import partial

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        button5 = QPushButton("Five")
        self.label = QLabel()

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.connect(button1, SIGNAL("clicked()"),
            partial(self.anyButton, "One"))
        self.connect(button2, SIGNAL("clicked()"),
            partial(self.anyButton, "Two"))
        self.connect(button3, SIGNAL("clicked()"),
            lambda who="Three": self.anyButton(who))
        self.connect(button4, SIGNAL("clicked()"), self.clicked)
        self.connect(button5, SIGNAL("clicked()"), self.clicked)

        self.setWindowTitle("Connections")

    def anyButton(self, who):
        self.label.setText("You clicked button '%s'" % who)

    def clicked(self):
        button = self.sender()
        if button is None or not isinstance(button, QPushButton):
            return
        self.label.setText("You clicked button '%s'" % button.text())

def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
