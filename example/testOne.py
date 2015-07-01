# python

# launchScript "C:/ie/ark/programs/modo/Kits/modo_widgetWrapper/example/testOne.py"

import lx
import modo

from PySide import QtGui
from PySide import QtCore

class Example(QtGui.QDialog):

	onClose = QtCore.Signal()

	def __init__(self, parent=None, **options):
		super(Example, self).__init__(parent)
		self.setGeometry(300, 300, 300, 100)
		self.setWindowTitle('Testing')

		print 'options:', options

		layout = QtGui.QHBoxLayout()

		# we still have access to the TD SDK
		scene = modo.Scene()
		filename = scene.filename

		self.textEdit = QtGui.QLineEdit(str(filename))
		self.textEdit.returnPressed.connect(self.enterPressed)

		layout.addWidget(self.textEdit)

		button = QtGui.QPushButton('Close')
		button.clicked.connect(self.test)
		layout.addWidget(button)

		self.setLayout(layout)

	def test(self):
		self.close()

	def enterPressed(self):
		print 'text entered:', self.textEdit.text()

	def closeEvent(self, event):
		self.onClose.emit()
		event.accept()




def main(**options):
	# This is where the magic happens!
	# The lx module is persistent so you can store stuff there
	# and access it in commands.  Think of it like a magical closet :)
	lx._widget = Example
	lx._widgetOptions = options

	# widgetWrapper creates whatever widget is set via lx._widget above
	# note we're using launchScript which allows for runtime blessing
	lx.eval('launchWidget')

	print 'widget instance:', lx._widgetInstance




if __name__ == '__main__':
	main(foo='bar')
