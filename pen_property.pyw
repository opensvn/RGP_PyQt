#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PenPropertiesDlg(QDialog):
    def __init__(self, parent=None):
        super(PenPropertiesDlg, self).__init__(parent)

        widthLabel = QLabel('&Width:')
        self.widthSpinbox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinbox)
        self.widthSpinbox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.widthSpinbox.setRange(0, 24)
        self.beveledCheckBox = QCheckBox('&Beveled edges')
        styleLabel = QLabel('&Style:')
        self.styleComboBox = QComboBox()
        self.styleComboBox.addItems(['Solid', 'Dashed', 'Dotted',
            'DashDotted', 'DashDotDotted'])
        okButton = QPushButton('&OK')
        cancelButton = QPushButton('Cancel')

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(self.widthSpinbox, 0, 1)
        layout.addWidget(self.beveledCheckBox, 0, 2)
        layout.addWidget(styleLabel, 1, 0)
        layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)

        self.connect(okButton, SIGNAL("clicked()"),
            self, SLOT("accept()"))
        self.connect(cancelButton, SIGNAL('clicked()'),
            self, SLOT('reject()'))
        self.setWindowTitle('Pen Properties')

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.width = 3
        self.beveled = True
        self.style = 'Dotted'

        self.button = QPushButton('Test')
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.connect(self.button, SIGNAL('clicked()'), 
            self.setPenProperties)

        self.setWindowTitle('Test')

    def setPenProperties(self):
        dialog = PenPropertiesDlg(self)
        dialog.widthSpinbox.setValue(self.width)
        dialog.beveledCheckBox.setChecked(self.beveled)
        dialog.styleComboBox.setCurrentIndex(
            dialog.styleComboBox.findText(self.style))
        if dialog.exec_():
            self.width = dialog.widthSpinbox.value()
            self.beveled = dialog.beveledCheckBox.isChecked()
            self.style = unicode(dialog.styleComboBox.currentText())
            self.updateData()

    def updateData(self):
        print 'width =', self.width
        print 'beveled =', self.beveled
        print 'style =', self.style

def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()