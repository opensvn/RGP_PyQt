#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        label1 = QLabel('Principal:')
        label2 = QLabel('Rate:')
        label3 = QLabel('Years:')
        self.label = QLabel()
        self.principalSpinBox = QDoubleSpinBox()
        self.principalSpinBox.setPrefix('$')
        self.principalSpinBox.setRange(0.01, 1000000.00)
        self.principalSpinBox.setValue(10000.00)
        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setSuffix('%')
        self.rateSpinBox.setRange(0.01, 100.00)
        self.rateSpinBox.setValue(3.00)
        self.yearSpinBox = QSpinBox()
        self.yearSpinBox.setRange(1, 100)
        self.yearSpinBox.setValue(1)

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.principalSpinBox, 0, 1)
        grid.addWidget(label2, 1, 0)
        grid.addWidget(self.rateSpinBox, 1, 1)
        grid.addWidget(label3, 2, 0)
        grid.addWidget(self.yearSpinBox, 2, 1)
        grid.addWidget(self.label, 3, 0)

        self.setLayout(grid)

        self.connect(self.principalSpinBox, SIGNAL('valueChanged(float)'),
            self.updateUi)
        self.connect(self.rateSpinBox, SIGNAL('valueChanged(float)'),
            self.updateUi)
        self.connect(self.yearSpinBox, SIGNAL('valueChanged(int)'),
            self.updateUi)

        self.setWindowTitle('Interset')

    def updateUi(self):
        principal = self.principalSpinBox.value()
        rate = self.rateSpinBox.value()
        years = self.yearSpinBox.value()
        amount = principal * ((1 + rate / 100.0) ** years)
        self.label.setText('Amount $%f' % amount)

def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
