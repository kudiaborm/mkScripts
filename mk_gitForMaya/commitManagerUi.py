__author__ = 'Marley Kudiabor'

import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

import os


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


class CommitManager(QtGui.QMainWindow):
    def __init__(self, parent=None):


        for qt in QtGui.QApplication([]).allWidgets():
            if qt.__class__.__name__ == self.__class__.__name__:
                qt.deleteLater()
        super(Window, self).__init__(parent=parent)
        self.resize(800, 400)
        self.move(300, 300)
        self.setWindowTitle('Simple')

        self.mainWidget = QtGui.QWidget(self)
        self.mainWidget.setGeometry(0, 0, 800, 400)
        self.mainLayout = QtGui.QGridLayout()
        self.mainWidget.setLayout(self.mainLayout)

        self.setStyleSheet("background: rgb(77, 80, 82)")

        self.commitNameField = QtGui.QLineEdit()
        self.commitMessageField = QtGui.QLineEdit()

        self.commitNameField.setPlaceholderText("Commit Name")
        self.commitMessageField.setPlaceholderText("Commit Details")

        self.commitButton = QtGui.QPushButton("Commit")
        self.cancelButton = QtGui.QPushButton("Cancel")

        self.layout().addWidget(self.commitNameField, 0, 0, 1, 2)
        self.layout().addWidget(self.commitMessageField, 0, 1, 1, 2)
        self.layout().addWidget(self.commitButton, 0, 2, 1, 1)
        self.layout().addWidget(self.cancelButton, 0, 2, 1, 1)

        self.show()

    def createMenuBar(self):
        pass
