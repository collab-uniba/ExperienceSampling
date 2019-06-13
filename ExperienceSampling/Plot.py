from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from ExperienceSampling.Utility import *


class Plot(QMainWindow):

    def __init__(self, app=None):

        QMainWindow.__init__(self)
        self.setWindowTitle("Retrospective")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)
        
        self.mpl = MyMplCanvas(self)
        layout.addWidget(self.mpl)


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        fig.tight_layout()

        self.compute_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def compute_figure(self):
        
        self.axes.spines['left'].set_position('center')
        self.axes.spines['bottom'].set_position('center')
        self.axes.spines['top'].set_position('center')
        self.axes.spines['right'].set_position('center')
            
        self.axes.set_xticks([], [])
        self.axes.set_yticks([], [])
        self.axes.set_xlim(0, 10)
        self.axes.set_ylim(0, 10)

        self.axes.text(5, 10.1, 'Very excited', horizontalalignment='center')
        self.axes.text(5, -.5, 'Very calm', horizontalalignment='center')
        self.axes.text(10, 5, 'Pleasant', verticalalignment='center', rotation=90)
        self.axes.text(-.5, 5, 'Unpleasant', verticalalignment='center', rotation=90)

        try:
            x,y = csv2numpy(csvFilePath())
            
            hist, xbins,ybins = np.histogram2d(y,x, bins=range(11))
            X,Y = np.meshgrid(xbins[:-1], ybins[:-1])
            X = X[hist != 0]; Y = Y[hist != 0]
            Z   = hist[hist != 0]
            
            self.axes.scatter(X, Y, s=Z/Z.max()*500, c=Z/Z.max(), cmap="winter_r", alpha=0.8)
        except IOError:
            pass

    def update_figure(self):
        
        self.axes.cla()
        self.compute_figure()
        self.draw()
