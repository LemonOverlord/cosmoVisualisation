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

    def __init__(self, parent: Canvas, h: int, w: int):

        self.parent = parent
        self.grid = parent.figure.add_gridspec(h, w, hspace=0, wspace=0)
        self.axis = self.grid.subplots(sharex=True, sharey=True)
        

class Plot:

    def __init__(self, parent: Axis, axis_id: int, xdata: list, ydata: list, *_, scale_x=10, scale_y):

        if xdata is None:
            data_x = []
        if ydata is None:
            data_y = []
        if axis_id is None:
            axis_id = 0

        self.parent = parent
        self.plot = parent.axis[axis_id].plot(xdata, ydata)
        self.scale_x = scale_x
        self.scale_y = scale_y

    def update(self, new_ydata: list, new_xdata: list):

        if new_ydata is None:
            new_ydata = []
        if new_xdata is None:
            new_xdata = []

        self.plot.set_ydata(new_ydata)
        self.plot.set_xdata(new_xdata)


x = numpy.linspace(0, 2 * numpy.pi, 10)
y = numpy.sin(x ** 2)

app = QApplication(sys.argv)
window = QWidget()
layout = QGridLayout(window)

layout.setVerticalSpacing(0)


canvas1 = Canvas(window)
layout.addWidget(canvas1, 0, 1, 2, 1)

axes1 = Axis(canvas1, 3, 1)
plot1_1 = axes1.axis[0].plot(x, y)
plot1_2 = axes1.axis[0].plot(y, x)


canvas2 = Canvas(window)
layout.addWidget(canvas2, 0, 0, 1, 1)

axis2 = Axis(canvas2, 1, 1)
plot2_1 = axis2.axis.plot(x, y)
plot2_2 = axis2.axis.plot(y, x)


canvas3 = Canvas(window)
layout.addWidget(canvas3, 1, 0, 1, 1)

axis3 = Axis(canvas3, 1, 1)
plot3 = axis3.axis.plot(x, y)


window.show()

sys.exit(app.exec_())
