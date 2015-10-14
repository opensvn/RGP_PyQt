#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        principalLabel = QLabel("Principal:")
        self.principalSpinBox = QDoubleSpinBox()
        self.principalSpinBox.setRange(1, 1000000000)
        self.principalSpinBox.setValue(1000)
        self.principalSpinBox.setPrefix("$ ")
        rateLabel = QLabel("Rate:")
        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setRange(1, 100)
        self.rateSpinBox.setValue(5)
        self.rateSpinBox.setSuffix(" %")
        yearsLabel = QLabel("Years:")
        self.yearsComboBox = QComboBox()
        self.yearsComboBox.addItem("1 year")
        self.yearsComboBox.addItems(["%d years" % x
                                     for x in range(2, 26)])
        amountLabel = QLabel("Amount")
        self.amountLabel = QLabel()

        grid = QGridLayout()
        grid.addWidget(principalLabel, 0, 0)
        grid.addWidget(self.principalSpinBox, 0, 1)
        grid.addWidget(rateLabel, 1, 0)
        grid.addWidget(self.rateSpinBox, 1, 1)
        grid.addWidget(yearsLabel, 2, 0)
        grid.addWidget(self.yearsComboBox, 2, 1)
        grid.addWidget(amountLabel, 3, 0)
        grid.addWidget(self.amountLabel, 3, 1)
        self.setLayout(grid)

        self.connect(self.principalSpinBox,
                     SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.rateSpinBox,
                     SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.yearsComboBox,
                SIGNAL("currentIndexChanged(int)"), self.updateUi)
        
        self.setWindowTitle("Interest")
        self.updateUi()


    def updateUi(self):
        """Calculates compound interest"""
        principal = self.principalSpinBox.value()
        rate = self.rateSpinBox.value()
        years = self.yearsComboBox.currentIndex() + 1
        amount = principal * ((1 + (rate / 100.0)) ** years)
        self.amountLabel.setText("$ %.2f" % amount)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()