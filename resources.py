# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication

from PySide6.QtSvg import QSvgRenderer

from PySide6.QtGui import QImage, QPainter, QIcon, QPixmap

from PySide6.QtCore import QFile, QIODevice, QDirIterator, QTextStream

try:
	import rc_resource
except ImportError:
	import resource_rc

icons = {}

sizes = [16, 24, 32, 48, 64]

def setupIcons():
	iterator = QDirIterator(':', QDirIterator.Subdirectories)
	while iterator.hasNext():
		path = iterator.next()
		if iterator.fileName().startswith('svg_'):
			file = QFile(path)
			if not file.open(QIODevice.ReadOnly | QIODevice.Text):
				print(f'Cannot open file: {file.errorString()}')
			else:
				svg = QTextStream(file).readAll().replace('#000000', QApplication.palette().text().color().name()).encode('utf-8')
				file.close()
				for i in sizes:
					renderer = QSvgRenderer(svg)
					image = QImage(i, i, QImage.Format_ARGB32)
					image.fill(0)
					painter = QPainter(image)
					renderer.render(painter)
					painter.end()
					icons[iterator.fileName().removeprefix('svg_') + '_' + str(i)] = QIcon(QPixmap.fromImage(image))
	for i in sizes:
		image = QImage(i, i, QImage.Format_ARGB32)
		image.fill(0)
		icons['blank_' + str(i)] = QIcon(QPixmap.fromImage(image))
