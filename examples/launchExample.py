


def launch(self, Dialog, **kwargs):
	# This is where the magic happens!
	# The lx module is persistent so you can store stuff there
	# and access it in commands.
	lx._widget = Dialog
	lx._widgetOptions = kwargs

	# widgetWrapper creates whatever widget is set via lx._widget above
	# note we're using launchScript which allows for runtime blessing
	lx.eval('launchWidget')

	try:
		return lx._widgetInstance
	except:
		return None
