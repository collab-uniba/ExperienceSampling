import matplotlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

matplotlib.use('Qt5Agg')
import numpy as np
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from ExperienceSampling.Utility import *


class Plot(QMainWindow):

    """
    A Qt5 window showing a retrospective diagram based on the Circumplex Model by James Russell.
    """

    def __init__(self, app=None):

        QMainWindow.__init__(self)
        self.setWindowTitle("Retrospective")
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint )

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.mpl = MyMplCanvas(self)
        layout.addWidget(self.mpl)

        self.allbutton = QRadioButton("View all days")
        self.singlebutton = QRadioButton("View single day: today")
        self.allbutton.clicked.connect(self.checkboxChange)
        self.singlebutton.clicked.connect(self.checkboxChange)
        self.allbutton.setChecked(True)
        layout.addWidget(self.allbutton)
        layout.addWidget(self.singlebutton)

        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(0)
        self.updateSliderRange()
        self.sl.setValue(0)
        self.sl.setTickInterval(1)
        self.sl.valueChanged.connect(self.sliderChange)
        self.sl.setDisabled(True)

        layout.addWidget(self.sl)

    def updateSliderRange(self):
        try:
            oldestDate = todayDate() - earliestDate(csvFilePath())
            rangeDays = oldestDate.days
            self.sl.setMaximum(rangeDays)
        except (IOError, ValueError):
            self.sl.setMaximum(0)


    def sliderChange(self):
        if (self.sl.value()==0):
            self.singlebutton.setText("View single day: today")
        else:
            self.singlebutton.setText("View single day: " + pastDate(todayDate(),self.sl.value()).isoformat() )
            pass
        self.updatePlot()

    def updatePlot(self):
        if self.allbutton.isChecked():
            self.mpl.update_figure()
        else:
            self.mpl.update_figure(pastDate(todayDate(),self.sl.value()))

    def checkboxChange(self):
        if self.allbutton.isChecked():
            self.sl.setDisabled(True)
        else:
            self.sl.setDisabled(False)
        self.updatePlot()


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


    def compute_figure(self, date=None):

        self.axes.spines['left'].set_position('center')
        self.axes.spines['bottom'].set_position('center')
        self.axes.spines['top'].set_position('center')
        self.axes.spines['right'].set_position('center')

        self.axes.set_xticks([], [])
        self.axes.set_yticks([], [])
        self.axes.set_xlim(0, 6)
        self.axes.set_ylim(0, 6)

        self.axes.text(3, 6.1, 'Excited', horizontalalignment='center')
        self.axes.text(3, -.3, 'Calm', horizontalalignment='center')
        self.axes.text(6.1, 3, 'Pleased', verticalalignment='center', rotation=90)
        self.axes.text(-.3, 3, 'Annoyed', verticalalignment='center', rotation=90)

        try:
            x,y = csv2numpy(csvFilePath(),date=date)

            hist, xbins,ybins = np.histogram2d(y,x, bins=range(7))
            X,Y = np.meshgrid(xbins[:-1], ybins[:-1])
            X = X[hist != 0]; Y = Y[hist != 0]
            Z   = hist[hist != 0]

            if (len(x)>0):
                self.axes.scatter(X, Y, s=Z/Z.max()*500, c=Z/Z.max(), cmap="winter_r", alpha=0.8)
        except IOError:
            pass

    def update_figure(self, date=None):

        self.axes.cla()
        self.compute_figure(date=date)
        self.draw()
