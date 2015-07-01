# Widget Wrapper for MODO

A robust widget wrapper for MODO that enables the display of PySide QWidgets and QDialogs in a fashion more in line with other PySide-based applications.  It works hand-in-hand with [modo_launchScript](https://github.com/IngenuityEngine/modo_launchScript).

## Installation
1. Hit Download ZIP on the right
2. From MODO go to System > Open Content Folder
3. Extract the contents of the zip to the Kits folder, should be Kits/widgetWrapper-master

## Use
See example/testOne.py for a working example

1. In your script's main() function set lx._widget to your QDialog or QWidget and lx._widgetOptions to any arguments that you'd like passed to the widget's ```__init__``` function:
```
	lx._widget = Example
	lx._widgetOptions = options
```

2. Launch the widget using launchWidget:
```
	lx.eval('launchWidget')
```
3. Get a reference to your newly created widget:
```
	widgetInstance = lx._widgetInstance
```
4. Bonus: If you close your dialog programatically, be sure to emit an ```onClose``` signal so the widget wrapper can close itself as well.  An example of this is included in example/testOne.py


## Benefits
- Matches the widget's desired size and position
- Hides the additional panels and title bars that MODO tries to add
- Sets the window title to match the widget's window title
- Closes automatically via onClose signal

## Drawbacks
- QWidgets work better as a base class than QDialog.  The first QDialog displays correctly but if _that_ dialog creates another dialog it will pop up two windows.  For this reason we suggest using QWidget as a base dialog class.
