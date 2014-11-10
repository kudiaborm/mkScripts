__author__ = 'Marley Kudiabor'

import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

import os

def listdir_fullpath(d):
	return [os.path.join(d, f) for f in os.listdir(d)]

class Window(QtGui.QMainWindow):

	def __init__(self, parent = None):
		super(Window, self).__init__(parent)
		self.resize(800, 400)
		self.move(300, 300)
		self.setWindowTitle('Simple')

		self.mainWidget = QtGui.QWidget(self)
		self.mainWidget.setGeometry(0, 0, 800, 400)
		self.mainLayout = QtGui.QVBoxLayout()
		self.mainWidget.setLayout(self.mainLayout)

		self.setStyleSheet("background: rgb(77, 80, 82)")
	def createMenuBar(self):
		pass
