from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os, sys, time, csv, datetime, shutil, platform, appdirs

from Utility import *

class Poll(QMainWindow):

    def __init__(self, app):

        self.app = app

        self.filepath = os.path.join(appdirs.user_data_dir('ExperienceSampling', 'UniBA'), 'data.csv')

        QMainWindow.__init__(self)
        self.setWindowTitle("Experience Sampling")

        # disable titlebar buttons, always on top
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)


        # ================ layout ================
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
        self.combobox1.addItems(['', 'Coding', 'Bugfixing', 'Testing', 'Design', 'Meeting', 'Email', 'Helping', 'Networking', 'Learning', 'Administrative tasks', 'Documentation'])
        self.combobox1.model().item(0).setEnabled(False)
        self.combobox1.activated.connect(self.checkPollComplete)

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
        [i.clicked.connect(self.checkPollComplete) for i in self.radioButtons1]
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
        [i.clicked.connect(self.checkPollComplete) for i in self.radioButtons2]
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
        self.textBox = QPlainTextEditSmall()
        self.textBox.setMinimumHeight(3*self.textBox.fontMetrics().lineSpacing())
        layout.addWidget(self.textBox)
        self.textBox.setPlaceholderText("Did you experience anything that might have affected your emotion during the last session?")

        layout.addItem(QSpacerItem(25, 25, QSizePolicy.Minimum, QSizePolicy.Fixed))

        #footer
        self.button1 = QPushButton("Done")
        self.button1.clicked.connect(self.submitForm)
        self.button1.setEnabled(False)
        layout.addWidget(self.button1,0,Qt.AlignHCenter)

  

    def showEvent(self, event):
        self.opened = int(time.time())
        self.app.stopPollTimer()
        self.show()

    def closeEvent(self, event):
        event.ignore()
        self.resetForm()
        self.hide()

    def hideEvent(self,event):
        self.app.startPollTimer()
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
        self.button1.setEnabled(False)

    def checkPollComplete(self):
        comboValid = self.combobox1.currentText() != ''
        
        radio1Valid = False
        for i in self.radioButtons1:
                if i.isChecked():
                    radio1Valid = True

        radio2Valid = False
        for i in self.radioButtons2:
                if i.isChecked():
                    radio2Valid = True

        if comboValid and radio1Valid and radio2Valid:
            self.button1.setEnabled(True)
      
    def submitForm(self):
        closed = int(time.time())
        activity = self.combobox1.currentText()

        valence = ''
        for i in self.radioButtons1:
            if i.isChecked():
                valence = i.text()
    
        arousal = ''
        for i in self.radioButtons2:
            if i.isChecked():
                arousal = i.text()

        note = self.textBox.toPlainText()

        poll = PollResult(self.opened, closed, activity, valence, arousal, note)
        self.app.writeToCSV(poll)
        self.hide()


class QPlainTextEditSmall(QPlainTextEdit):
    def __init__(self, parent=None):
        QPlainTextEdit.__init__(self, parent)
    
    def sizeHint(self):
        return QSize(1,1)
    
    def minimumSizeHint(self):
        return QSize(1,1)

class PollResult:
    def __init__(self, opened, closed, activity, valence, arousal, note=''):
        self.opened = opened
        self.closed = closed        
        self.activity = activity
        self.valence = valence
        self.arousal = arousal
        self.note = note


