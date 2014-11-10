__author__ = 'Marley Kudiabor'

import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore

import sys

import commitManagerUi
reload(commitManagerUi)

def main():
	try:
		newWindow.close()

	except:
		app = QtGui.QApplication(sys.argv)

		newWindow = commitManagerUi.Window()

		newWindow.show()
		newWindow.activateWindow()
		sys.exit(app.exec_())
		QtCore.QObject.connect(newWindow,QtCore.SIGNAL("lastWindowClosed()"),app,QtCore.SLOT("quit()"))



main()
