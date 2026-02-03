# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QCheckBox

from PySide6.QtCore import Slot, QRegularExpression

@Slot()
def toggleCheckBoxes(self, arg, isRegex=False):
	if isinstance(arg, list):
		checkBoxes = arg
	else:
		if isRegex:
			checkBoxes = self.findChildren(QCheckBox, QRegularExpression(arg))
		else:
			checkBoxes = self.findChildren(QCheckBox, arg)
	checked = []
	for checkBox in checkBoxes:
		if checkBox.isEnabled():
			checked.append(checkBox.isChecked())
		else:
			checked.append(True)
	for checkBox in checkBoxes:
		if checkBox.isEnabled():
			checkBox.setChecked(True if False in checked else False)
