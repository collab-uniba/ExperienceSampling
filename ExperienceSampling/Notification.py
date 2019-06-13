from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ExperienceSampling.Utility import *


class Notification(QMainWindow):

    def __init__(self, app):

        self.app = app

        QMainWindow.__init__(self)
        self.setWindowTitle("Experience Sampling")

        # set no borders, no titlebar, no taskbar icon, always on top
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        # ================ layout ================
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        image = QLabel()
        pm = QPixmap(resource_path("data/notify.png"))
        pm = pm.scaled(64,64)
        image.setPixmap(pm)
        layout.addWidget(image, 0, Qt.AlignCenter)

        label1 = QLabel('How are you feeling?<br>Click here to open the popup')
        label1.setStyleSheet("font-size: 12pt;")
        layout.addWidget(label1)

        answerLayout = QVBoxLayout()
        layout.addLayout(answerLayout)

        self.button1 = QPushButton("Dismiss")
        self.button2 = QPushButton("Postpone: " + str(self.app.postponeTime) + " min")
        self.button1.clicked.connect(self.dismissAction)
        self.button2.clicked.connect(self.postponeAction)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(5)
        self.slider.setMaximum(120)
        self.slider.setValue(self.app.postponeTime)
        self.slider.valueChanged.connect(self.sliderChanged)

        answerLayout.addWidget(self.button1)
        answerLayout.addWidget(self.button2)
        answerLayout.addWidget(self.slider)

        # ================ trayicon ================

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(resource_path("data/tray.png")))
        tray_menu = QMenu()
        self.tray_icon.setContextMenu(tray_menu)
        
        plot_action = QAction("Show Retrospective", self)
        show_action = QAction("Show Emotion Pop-up", self)
        self.toggle_action = QAction("Disable timer", self)
        set_action = QAction("Set timer", self)
        export_action = QAction("Export to csv", self)
        about_action = QAction("About", self)
        quit_action = QAction("Quit", self)
        
        plot_action.triggered.connect(self.plotEvent)
        show_action.triggered.connect(self.showPollEvent)
        self.toggle_action.triggered.connect(self.toggleAction)
        set_action.triggered.connect(self.setAction)
        export_action.triggered.connect(self.exportAction)
        about_action.triggered.connect(self.about)
        quit_action.triggered.connect(self.quitEvent)

        tray_menu.addAction(plot_action)
        tray_menu.addAction(show_action)
        tray_menu.addAction(self.toggle_action)
        tray_menu.addAction(set_action)
        tray_menu.addAction(export_action)
        tray_menu.addAction(about_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.show()
        self.tray_icon.activated.connect(self.updateTray)


    def about(self):
        QMessageBox.about(self, "About",
        """Experience Sampling, 2019
        
Giuseppe Antonio Nanna (h3r0n)
Arcangelo Saracino (Arkango)
        """)

    def resizeEvent(self, event):
        width = self.width()
        height = self.height()

        screen = QDesktopWidget().screenGeometry()
        x = screen.width() - self.width()
        self.move(x, 150)

    def showEvent(self,event):
        self.app.stopPollTimer()
        self.app.stopPostponeTimer()
        self.show()

    def quitEvent(self):
        self.tray_icon.hide()
        qApp.quit()

    def showPollEvent(self):
        self.hide()
        self.app.showPoll()

    def plotEvent(self):
        self.app.showPlot()

    def mousePressEvent(self, ev):
        self.hide()
        self.app.showPoll()

    def sliderChanged(self):
        value = self.slider.value()
        self.button2.setText("Postpone: " + str(value) + " min")
        self.app.setPostponeTimer(value)

    def dismissAction(self):
        self.hide()
        self.app.pollTimerEnabled = False
        self.app.stopPollTimer()

    def postponeAction(self):
        self.hide()
        self.app.startPostponeTimer()
        #self.app.setPollTimer()

    def exportAction(self):
        self.app.exportCSV()

    def setAction(self):
        i, okPressed = QInputDialog.getInt(self, "Set timer","Minutes:", self.app.pollTime, 0, 100, 1)
        if okPressed and i>0:
            self.app.setPollTimer(i)

    def toggleAction(self):
        if self.app.pollTimerEnabled:
            self.app.pollTimerEnabled = False
            self.app.stopPollTimer()
        else:
            self.app.pollTimerEnabled = True
            self.app.startPollTimer()

    def updateTray(self):
        if self.app.pollTimerEnabled:
            self.toggle_action.setText("Disable timer")
        else:
            self.toggle_action.setText("Enable timer")