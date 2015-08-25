#!/usr/bin/env python
# There's an error

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AddEdit(QDialog):
    def __init__(self, stringlist, parent=None):
        super(AddEdit, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.stringlist = stringlist[:]

        self.label = QLabel('Add Fruit')
        self.inputDialog = QInputDialog()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok
            |QDialogButtonBox.Cancel)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.inputDialog)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

        self.connect(buttonBox, SIGNAL('accepted()'),
            self, SLOT('accept()'))
        self.connect(buttonBox, SIGNAL('rejected()'),
            self, SLOT('reject()'))

        self.setWindowTitle('Add Fruit')

    def accept(self):
        new_fruit = self.inputDialog.getText()
        self.stringlist.append(new_fruit)
        QDialog.accept(self)

    def reject(self):
        self.accept()

class StringListDlg(QDialog):
    def __init__(self, name, slist, parent=None):
        super(StringListDlg, self).__init__(parent)

        self.name = name
        self.stringlist = slist

        self.addButton = QPushButton('&Add...')
        self.editButton = QPushButton('&Edit...')
        self.removeButton = QPushButton('&Remove...')
        self.upButton = QPushButton('&Up')
        self.downButton = QPushButton('&Down')
        self.sortButton = QPushButton('&Sort')
        self.closeButton = QPushButton('Close')
        self.listWidget = QListWidget()

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.editButton)
        buttonLayout.addWidget(self.removeButton)
        buttonLayout.addWidget(self.upButton)
        buttonLayout.addWidget(self.downButton)
        buttonLayout.addWidget(self.sortButton)
        buttonLayout.addWidget(self.closeButton)

        layout = QHBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)

        self.connect(self.addButton, SIGNAL('clicked()'), self.addFruit)
        self.setWindowTitle('Edit ' + self.name + ' List')

        self.refresh()

    def addFruit(self):
        dialog = AddEdit(self.stringlist)
        if dialog.exec_():
            self.stringlist = dialog.stringlist[:]
            self.refresh()

    def refresh(self):
        for fruit in self.stringlist:
            self.listWidget.addItem(fruit)


def main():
    fruit = ['Banana', 'Apple', 'Elderberry', 'Clementine', 'Fig',
        'Guava', 'Mango', 'Honeydew Melon', 'Date', 'Watermelon',
        'Tangerine', 'Ugli Fruit', 'Juniperberry', 'kiwi',
        'Lemon', 'Nectarine', 'Plum', 'Raspberry', 'Strawberry',
        'Orange']
    app = QApplication(sys.argv)
    form = StringListDlg('Fruit', fruit)
    form.exec_()
    print '\n'.join([unicode(x) for x in form.stringlist])

if __name__ == '__main__':
    main()