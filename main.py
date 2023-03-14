import sys

import numpy
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Canvas(QWidget):

    def __init__(self, parent: QMainWindow):

        super(Canvas, self).__init__(parent)

        self.figure = Figure(figsize=(10, 10), dpi=100)
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.setMinimumSize(400, 300)

        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)


class Axis:

    def __init__(self, parent: QWidget, h: int, w: int):

        self.parent = parent
        self.grid = parent.figure.add_gridspec(h, w, hspace=0, wspace=0)
        self.axis = self.grid.subplots(sharex=True, sharey=True)


x = numpy.linspace(0, 2 * numpy.pi, 10)
y = numpy.sin(x ** 2)

app = QApplication(sys.argv)
window = QWidget()
layout = QGridLayout(window)

layout.setVerticalSpacing(0)


accel_canvas = Canvas(window)
layout.addWidget(accel_canvas, 0, 1, 2, 1)

accel_axes = Axis(accel_canvas, 3, 1)
accel_plot1 = accel_axes.axis[0].plot(x, y)


bar_canvas = Canvas(window)
layout.addWidget(bar_canvas, 0, 0, 1, 1)

bar_axis = Axis(bar_canvas, 1, 1)
bar_plot = bar_axis.axis.plot(x, y)


temp_canvas = Canvas(window)
layout.addWidget(temp_canvas, 1, 0, 1, 1)

temp_axis = Axis(temp_canvas, 1, 1)
temp_plot = temp_axis.axis.plot(x, y)


window.show()

sys.exit(app.exec_())
