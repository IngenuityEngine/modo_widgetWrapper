# python

import lx
import lxu
import lxifc

from PySide import QtGui
from PySide import QtCore

class WidgetHolder(lxifc.CustomView):
	'''
	Custom viewport that imports and wraps the PySide widget
	'''

	def customview_Init(self, pane):
		'''
		Initialize the viewport, add the PySide widget.
		'''

		# try to get the widget and it's options from the lx module
		if hasattr(lx, '_widget'):
			if hasattr(lx, '_widgetOptions'):
				options = lx._widgetOptions
			else:
				options = {}
			widget = lx._widget(**options)
		else:
			raise Exception('No _widget found on lx. \
				Be sure to set this before running widgetWrapper')

		if not pane:
			return False

		# Get the pane
		customPane = lx.object.CustomPane(pane)

		if not customPane.test():
			return False

		# Get the parent QWidget
		parent = customPane.GetParent()
		parentWidget = lx.getQWidget(parent)

		# Check that it succeeded
		if not parentWidget:
			return False

		# this fills in the background of widgets to hide the
		# other panel stuff that I can't for the life of me
		# figure out how to remove :\
		widget.setAttribute(QtCore.Qt.WA_StyledBackground, True)

		# make a new simple layout and add our widget
		layout = QtGui.QGridLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.addWidget(widget)

		panel = parentWidget.parent().parent()
		panel.setLayout(layout)

		# that nesting!
		dialog = parentWidget.parent().parent().parent()
		# move the parent dialog and set it's geometry
		# to match the widget
		dialog.setGeometry(widget.geometry())
		dialog.move(widget.x(), widget.y())
		dialog.setWindowTitle(widget.windowTitle())

		# our dialogs all emit an onClose event when closed
		try:
			widget.onClose.connect(dialog.close)
		except:
			pass

		lx._widgetResult = widget




class LaunchWidget(lxu.command.BasicCommand):

	def basic_Execute(self, msg, flags):
		# create a new window and set it's view to our custom view
		lx.eval('layout.create width:600 height:400 class:normal')
		lx.eval('customview.view pyside.widgetHolder')




def main():
	# only bless once (we run this as a way of launching windows)
	try:
		lx.bless(WidgetHolder, 'pyside.widgetHolder')
		lx.bless(LaunchWidget, 'launchWidget')
	except:
		pass

main()
