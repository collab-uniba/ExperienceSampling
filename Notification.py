#!/usr/bin/env python3


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys, os

from Utility import *

class Notification(QMainWindow):

    def __init__(self):

        self.value_changed

        QMainWindow.__init__(self)
        self.setWindowTitle("Experience Sampling")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        image = QLabel()
        pm = QPixmap(resource_path("icons/icon_b_128.png"))
        pm = pm.scaled(64,64)
        image.setPixmap(pm)
        layout.addWidget(image, 0, Qt.AlignCenter)

        label1 = QLabel('How are you feeling?<br>Click here to open the popup')
        label1.setStyleSheet("font-size: 12pt;")
        layout.addWidget(label1)

        answerLayout = QVBoxLayout()
        layout.addLayout(answerLayout)

        self.button1 = QPushButton("Dismiss")
        self.button2 = QPushButton("Postpone: 60 min")
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(5)
        self.slider.setMaximum(120)
        self.slider.setValue(60)
        self.slider.valueChanged.connect(self.value_changed)

        answerLayout.addWidget(self.button1)
        answerLayout.addWidget(self.button2)
        answerLayout.addWidget(self.slider)

    def value_changed(self):
        value = self.slider.value()
        self.button2.setText("Postpone: " + str(value) + " min")


    def resizeEvent(self, event):
        width = self.width()
        height = self.height()

        screen = QDesktopWidget().screenGeometry()
        x = screen.width() - self.width()
        self.move(x, 150)

    def mousePressEvent(self, ev):
        print("lol")


if __name__ == "__main__":

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    ntfy = Notification()
    ntfy.show()

    sys.exit(app.exec_())