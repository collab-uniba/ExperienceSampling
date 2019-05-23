#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os, sys, time, csv, datetime, shutil

class MainWindow(QMainWindow):

    def __init__(self, time=60):

        self.filepath = os.path.join(os.getcwd(), datetime.date.today().isoformat() + '.csv')

        self.timerEnabled = True
        self.timeout = time
        self.timer = QTimer()
        self.timer.timeout.connect(self.show)

        QMainWindow.__init__(self)
        self.setWindowTitle("Experience Sampling")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        #combobox
        label1 = QLabel('In which activity have you mainly been involved since the last notification?')
        label1.setAlignment(Qt.AlignCenter)
        label1.setStyleSheet("font-size: 12pt; font-weight: bold;")
        layout.addWidget(label1)
        self.combobox1 = QComboBox()
        layout.addWidget(self.combobox1, 0, Qt.AlignHCenter)
        self.combobox1.addItems(['', 'Coding', 'Taking a break', 'Debugging'])
        self.combobox1.model().item(0).setEnabled(False)

        layout.addItem(QSpacerItem(25, 25, QSizePolicy.Minimum, QSizePolicy.Fixed))

        #howDoYouFeel1
        label2 = QLabel('How do you feel right now?')
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet("font-size: 12pt; font-weight: bold;")
        layout.addWidget(label2)
        feel1Group = QGroupBox()
        layout.addWidget(feel1Group)
        feel1GroupLayout = QVBoxLayout()
        feel1Group.setLayout(feel1GroupLayout)
        feel1ImgLayout = QHBoxLayout()
        feel1GroupLayout.addLayout(feel1ImgLayout)
        feel1RadioLayout = QHBoxLayout()
        feel1GroupLayout.addLayout(feel1RadioLayout)
        feel1LabelLayout = QHBoxLayout()
        feel1GroupLayout.addLayout(feel1LabelLayout)

        #images
        images1 = []
        for i in range(1,6):
            j = QLabel()
            images1.append(j)
            j.setPixmap(QPixmap(resource_path("icons/V" + str(i) + ".png")))

        [feel1ImgLayout.addWidget(i, 0, Qt.AlignCenter) for i in images1]

        #radio buttons
        self.radioButtons1 = []
        [self.radioButtons1.append(QRadioButton(str(i))) for i in range(1,10)] 
        [feel1RadioLayout.addWidget(i) for i in self.radioButtons1]

        #labels
        label1_1 = QLabel("Very unpleasant")
        feel1LabelLayout.addWidget(label1_1)
        label1_2 = QLabel("Neutral")
        label1_2.setAlignment(Qt.AlignCenter)
        feel1LabelLayout.addWidget(label1_2)
        label1_3 = QLabel("Very pleasant")
        label1_3.setAlignment(Qt.AlignRight)
        feel1LabelLayout.addWidget(label1_3)

        #howDoYouFeel2
        feel2Group = QGroupBox()
        layout.addWidget(feel2Group)
        feel2GroupLayout = QVBoxLayout()
        feel2Group.setLayout(feel2GroupLayout)
        feel2ImgLayout = QHBoxLayout()
        feel2GroupLayout.addLayout(feel2ImgLayout)
        feel2RadioLayout = QHBoxLayout()
        feel2GroupLayout.addLayout(feel2RadioLayout)
        feel2LabelLayout = QHBoxLayout()
        feel2GroupLayout.addLayout(feel2LabelLayout)

        #images
        images2 = []
        for i in range(1,6):
            j = QLabel()
            images2.append(j)
            j.setPixmap(QPixmap(resource_path("icons/A" + str(i) + ".png")))

        [feel2ImgLayout.addWidget(i, 0, Qt.AlignCenter) for i in images2]

        #radio buttons
        self.radioButtons2 = []
        [self.radioButtons2.append(QRadioButton(str(i))) for i in range(1,10)] 
        [feel2RadioLayout.addWidget(i) for i in self.radioButtons2]

        #labels
        label2_1 = QLabel("Very calm")
        feel2LabelLayout.addWidget(label2_1)
        label2_2 = QLabel("Neutral")
        label2_2.setAlignment(Qt.AlignCenter)
        feel2LabelLayout.addWidget(label2_2)
        label2_3 = QLabel("Very excited")
        label2_3.setAlignment(Qt.AlignRight)
        feel2LabelLayout.addWidget(label2_3)

        layout.addItem(QSpacerItem(25, 25, QSizePolicy.Minimum, QSizePolicy.Fixed))

        #notes
        label3 = QLabel('Notes (optional)')
        label3.setStyleSheet("font-size: 10pt; font-weight: bold;")
        layout.addWidget(label3)
        self.textBox = QPlainTextEdit()
        self.textBox.setMinimumHeight(3*self.textBox.fontMetrics().lineSpacing())
        layout.addWidget(self.textBox)
        self.textBox.setPlaceholderText("Did you experience anything that might have affected your emotion during the last session?")

        layout.addItem(QSpacerItem(25, 25, QSizePolicy.Minimum, QSizePolicy.Fixed))

        #footer
        doneLayout = QHBoxLayout()
        layout.addLayout(doneLayout)
        self.label5 = QLabel()
        doneLayout.addWidget(self.label5)
        self.button1 = QPushButton("Done")
        self.button1.clicked.connect(self.writeToCSV)
        doneLayout.addWidget(self.button1,0,Qt.AlignHCenter)
        label4 = QLabelLink("Export to csv...")
        label4.setAlignment(Qt.AlignRight)
        label4.clicked.connect(self.saveCSV)
        doneLayout.addWidget(label4)

        #tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(resource_path("icons/status.png")))
        
        #tray logic
        show_action = QAction("Show", self)
        hide_action = QAction("Hide", self)
        set_action = QAction("Set timer", self)
        start_action = QAction("Enable timer", self)
        stop_action = QAction("Disable timer", self)
        quit_action = QAction("Exit", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        set_action.triggered.connect(self.setTimer)
        start_action.triggered.connect(self.enableTimer)
        stop_action.triggered.connect(self.disableTimer)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(set_action)
        tray_menu.addAction(start_action)
        tray_menu.addAction(stop_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.enableTimer()

    def showEvent(self, event):
        self.openTime = int(time.time())
        self.timer.stop()
        self.show()

    def closeEvent(self, event):
        event.ignore()
        self.resetForm()
        self.hide()

    def hideEvent(self,event):
        self.startTimer()
        self.resetForm()
        self.hide()
        
    def resetForm(self):
        self.combobox1.setCurrentIndex(0)
        for i in self.radioButtons1:
            i.setAutoExclusive(False)
            i.setChecked(False)
            i.setAutoExclusive(True)
        for i in self.radioButtons2:
            i.setAutoExclusive(False)
            i.setChecked(False)
            i.setAutoExclusive(True)
        self.textBox.setPlainText('')

    def startTimer(self):
        if self.timerEnabled and self.timeout>0:
            self.timer.start(self.timeout*1000*60)

    def enableTimer(self):
        if self.timeout>0:
            self.timerEnabled = True
            self.startTimer()
            self.label5.setText("Timer: " + str(self.timeout) + " min")
        else:
            self.disableTimer()

    def disableTimer(self):
        self.timerEnabled = False
        self.timer.stop()
        self.label5.setText("Timer: disabled")

    def writeToCSV(self):

        self.filepath = os.path.join(os.getcwd(), datetime.date.today().isoformat() + '.csv')

        with open(self.filepath, mode='a', newline='') as data:
            data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            submitTime = int(time.time())
            activity = self.combobox1.currentText()
            notes = self.textBox.toPlainText()
            
            valence = ''
            j = 0
            for i in self.radioButtons1:
                j += 1
                if i.isChecked():
                    valence = i.text()

            arousal = ''
            j = 0
            for i in self.radioButtons2:
                j += 1
                if i.isChecked():
                    arousal = i.text()

            data_writer.writerow([self.openTime,submitTime,activity,valence,arousal,notes])
            self.hide()

    def saveCSV(self):
        name = QFileDialog.getSaveFileName(self, 'Salva dati', os.getcwd(), 'CSV(*.csv)')
        shutil.copyfile(self.filepath, name[0])

    def setTimer(self):
        i, okPressed = QInputDialog.getInt(self, "Set timer","Minutes:", self.timeout, 0, 100, 1)
        if okPressed and i>0:
            self.timeout = i
            self.disableTimer()
            self.enableTimer()

class QLabelLink(QLabel):
    clicked=pyqtSignal()
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setStyleSheet("color: blue; text-decoration: underline;")

    def mousePressEvent(self, ev):
        self.clicked.emit()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    mw = MainWindow(60)
    mw.show()

    sys.exit(app.exec_())

