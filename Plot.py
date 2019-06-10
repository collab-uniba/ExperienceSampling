#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, random, matplotlib

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

from numpy import arange, sin, pi
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


from Utility import *


class Plot(QMainWindow):

    def __init__(self):

        self.value_changed

        QMainWindow.__init__(self)
        self.setWindowTitle("Russell Circumplex Model")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)
        
        layout.addWidget(MyMplCanvas(self))
        

    def value_changed(self):
        value = self.slider.value()
        self.button2.setText("Postpone: " + str(value) + " min")

    def mousePressEvent(self, ev):
        print("lol")


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        fig.tight_layout()

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def compute_initial_figure(self):

        self.axes.spines['left'].set_position('center')
        self.axes.spines['bottom'].set_position('center')
        self.axes.spines['top'].set_position('center')
        self.axes.spines['right'].set_position('center')
        
        self.axes.set_xticks([], [])
        self.axes.set_yticks([], [])
        self.axes.set_xlim(0, 10)
        self.axes.set_ylim(0, 10)

        self.axes.text(5, 10.1, 'Aroused', horizontalalignment='center')
        self.axes.text(5, -.5, 'Not aroused', horizontalalignment='center')
        self.axes.text(10, 5, 'Pleasant', verticalalignment='center', rotation=90)
        self.axes.text(-.5, 5, 'Unpleasant', verticalalignment='center', rotation=90)
        
        x = np.random.randint(1, 10, size=50)
        y = np.random.randint(1, 10, size=50)
        
        hist, xbins,ybins = np.histogram2d(y,x, bins=range(11))
        X,Y = np.meshgrid(xbins[:-1], ybins[:-1])
        X = X[hist != 0]; Y = Y[hist != 0]
        Z   = hist[hist != 0]
        
        self.axes.scatter(X, Y, s=Z/Z.max()*100, c = Z/Z.max(), cmap="winter_r", alpha=0.8)


if __name__ == "__main__":

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    print(QApplication.desktop().availableGeometry())

    app.setWindowIcon(QIcon(resource_path("icons/status.png")))
    plt = Plot()
    plt.show()

    sys.exit(app.exec_())