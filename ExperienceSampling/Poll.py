from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import time

from ExperienceSampling.Utility import *


class Poll(QMainWindow):

    def __init__(self, app):

        self.app = app

        QMainWindow.__init__(self)
        self.setWindowTitle("Experience Sampling")

        # disable titlebar buttons, always on top
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint )

        self.activities = ['', 'Coding', 'Bugfixing', 'Testing', 'Design', 'Meeting', 'Email', 'Helping', 'Networking', 'Learning', 'Administrative tasks', 'Documentation']
        self.productivityLevel = ['Very low','Below average','Average','Above average','Very high']
        # ================ layout ================
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)


        activityLayout = QHBoxLayout()
        layout.addLayout(activityLayout)

        #combobox
        label1 = QLabel('In which activity are you involved?   ')
        label1.setStyleSheet("font-size: 12pt; font-weight: bold;")
        activityLayout.addWidget(label1, 0, Qt.AlignRight)
        self.combobox1 = QComboBox()
        activityLayout.addWidget(self.combobox1, 0, Qt.AlignLeft)
        self.combobox1.addItems(self.activities)
        self.combobox1.model().item(0).setEnabled(False)
        self.combobox1.activated.connect(self.checkPollComplete)

        layout.addItem(QSpacerItem(1, 3, QSizePolicy.Minimum, QSizePolicy.Fixed))

        #howDoYouFeel1
        label2 = QLabel('How do you feel now?')
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

        feel1Group.setToolTip('''The valence level measures how pleasant or unpleasant one feels about something and range from a frown to a smile.
If you feel completely annoyed, unhappy, unsatisfied, melancholic, despaired, bored, you can indicate this by choosing the figure at the left.
The other end of the scale is when you feel completely happy, pleased, satisfied, contented, and hopeful.
The figures also allow you to describe intermediate feelings of pleasure, by choosing any other pictures.''')  

        #images
        images1 = []
        for i in range(1,6):
            j = QLabel()
            images1.append(j)
            j.setPixmap(QPixmap(resource_path("data/V" + str(i) + ".png")))

        [feel1ImgLayout.addWidget(i, 0, Qt.AlignCenter) for i in images1]

        #radio buttons
        self.radioButtons1 = []
        [self.radioButtons1.append(QRadioButton(str(i))) for i in range(1,6)]
        [i.clicked.connect(self.checkPollComplete) for i in self.radioButtons1]
        [feel1RadioLayout.addWidget(i,0, Qt.AlignCenter) for i in self.radioButtons1]

        #labels
        label1_1 = QLabel("Annoyed")
        feel1LabelLayout.addWidget(label1_1)
        label1_3 = QLabel("Pleased")
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

        feel2Group.setToolTip('''The arousal level, measures how energized or soporific one feels.
At one extreme of the scale you feel calm, relaxed, sluggish, dull, sleepy, and un-aroused.
On the other hand, at the other end of the scale, you feel completely excited, stimulated, frenzied, jittery, wide-awake, aroused.
You can represent intermediate levels by choosing any of the other figures''')

        #images
        images2 = []
        for i in range(1,6):
            j = QLabel()
            images2.append(j)
            j.setPixmap(QPixmap(resource_path("data/A" + str(i) + ".png")))

        [feel2ImgLayout.addWidget(i, 0, Qt.AlignCenter) for i in images2]

        #radio buttons
        self.radioButtons2 = []
        [self.radioButtons2.append(QRadioButton(str(i))) for i in range(1,6)]
        [i.clicked.connect(self.checkPollComplete) for i in self.radioButtons2]
        [feel2RadioLayout.addWidget(i,0, Qt.AlignCenter) for i in self.radioButtons2]

        #labels
        label2_1 = QLabel("Calm")
        feel2LabelLayout.addWidget(label2_1)
        label2_3 = QLabel("Excited")
        label2_3.setAlignment(Qt.AlignRight)
        feel2LabelLayout.addWidget(label2_3)


        # howDoYouFeel3
        feel3Group = QGroupBox()
        layout.addWidget(feel3Group)
        feel3GroupLayout = QVBoxLayout()
        feel3Group.setLayout(feel3GroupLayout)
        feel3ImgLayout = QHBoxLayout()
        feel3GroupLayout.addLayout(feel3ImgLayout)
        feel3RadioLayout = QHBoxLayout()
        feel3GroupLayout.addLayout(feel3RadioLayout)
        feel3LabelLayout = QHBoxLayout()
        feel3GroupLayout.addLayout(feel3LabelLayout)

        feel3Group.setToolTip('''The dominance is the dimension of controlled vs. in-control.
At one end of the scale you have feelings characterized as completely controlled, influenced, cared-for, awed, submissive, and guided.
At the other extreme of this scale, you feel completely controlling, influential, in control, important, dominant, and autonomous.
If you feel neither in control nor controlled you should chose middle picture.''')

        # images
        images3 = []
        for i in range(1, 6):
            j = QLabel()
            images3.append(j)
            j.setPixmap(QPixmap(resource_path("data/D" + str(i) + ".png")))

        [feel3ImgLayout.addWidget(i, 0, Qt.AlignCenter) for i in images3]

        # radio buttons
        self.radioButtons3 = []
        [self.radioButtons3.append(QRadioButton(str(i))) for i in range(1, 6)]
        [i.clicked.connect(self.checkPollComplete) for i in self.radioButtons3]
        [feel3RadioLayout.addWidget(i, 0, Qt.AlignCenter) for i in self.radioButtons3]

        # labels
        label3_1 = QLabel("Controlled")
        feel3LabelLayout.addWidget(label3_1)
        label3_3 = QLabel("In control")
        label3_3.setAlignment(Qt.AlignRight)
        feel3LabelLayout.addWidget(label3_3)



        layout.addItem(QSpacerItem(1, 3, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # combobox2

        productivityLayout = QHBoxLayout()
        layout.addLayout(productivityLayout)

        label1 = QLabel('My productivity is:  ')
        label1.setAlignment(Qt.AlignCenter)
        label1.setStyleSheet("font-size: 12pt; font-weight: bold;")
        productivityLayout.addWidget(label1)

        layout.addItem(QSpacerItem(1, 3, QSizePolicy.Minimum, QSizePolicy.Fixed))
        productivityGroup = QGroupBox()
        productivityLayout.addWidget(productivityGroup)
        productivityGroupLayout = QHBoxLayout()
        productivityGroup.setLayout(productivityGroupLayout)
        
        self.radioButtons4 = []
        [self.radioButtons4.append(QRadioButton(str(i))) for i in self.productivityLevel]
        [i.clicked.connect(self.checkPollComplete) for i in self.radioButtons4]
        [productivityGroupLayout.addWidget(i, 0, Qt.AlignCenter) for i in self.radioButtons4]



        #notes
        label3 = QLabel('Notes (optional)')
        label3.setStyleSheet("font-size: 12pt; font-weight: bold;")
        layout.addWidget(label3)
        self.textBox = QPlainTextEditSmall()
        self.textBox.setMinimumHeight(2*self.textBox.fontMetrics().lineSpacing())
        layout.addWidget(self.textBox)
        self.textBox.setPlaceholderText("Did you experience anything that might have affected your emotion during the last session?")

        layout.addItem(QSpacerItem(1, 3, QSizePolicy.Minimum, QSizePolicy.Fixed))

        #footer
        self.button1 = QPushButton("Done")
        self.button1.clicked.connect(self.submitForm)
        self.button1.setEnabled(False)
        layout.addWidget(self.button1,0,Qt.AlignHCenter)



    def showEvent(self, event):
        self.opened = int(time.time())
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
        #self.combobox2.setCurrentIndex(0)
        for i in self.radioButtons1:
            i.setAutoExclusive(False)
            i.setChecked(False)
            i.setAutoExclusive(True)
        for i in self.radioButtons2:
            i.setAutoExclusive(False)
            i.setChecked(False)
            i.setAutoExclusive(True)
        for i in self.radioButtons3:
            i.setAutoExclusive(False)
            i.setChecked(False)
            i.setAutoExclusive(True)
        for i in self.radioButtons4:
            i.setAutoExclusive(False)
            i.setChecked(False)
            i.setAutoExclusive(True)
        self.textBox.setPlainText('')
        self.button1.setEnabled(False)

    def checkPollComplete(self):
        comboValid = self.combobox1.currentText() != ''
        #comboValid2 = self.combobox2.currentText() != ''

        radio1Valid = False
        for i in self.radioButtons1:
                if i.isChecked():
                    radio1Valid = True

        radio2Valid = False
        for i in self.radioButtons2:
                if i.isChecked():
                    radio2Valid = True

        radio3Valid = False
        for i in self.radioButtons3:
                if i.isChecked():
                    radio3Valid = True

        radio4Valid = False
        for i in self.radioButtons4:
                if i.isChecked():
                    radio4Valid = True

        if comboValid and radio1Valid and radio2Valid and radio3Valid and radio4Valid:
            self.button1.setEnabled(True)
            self.button1.repaint(self.button1.rect())   # Qt bug workaround: https://github.com/3ll3d00d/beqdesigner/issues/56
      
    def submitForm(self):
        closed = int(time.time())
        activity = self.combobox1.currentText()
        #productivity = self.combobox2.currentText()

        valence = ''
        for i in self.radioButtons1:
            if i.isChecked():
                valence = i.text()
    
        arousal = ''
        for i in self.radioButtons2:
            if i.isChecked():
                arousal = i.text()

        dominance = ''
        for i in self.radioButtons3:
            if i.isChecked():
                dominance = i.text()

        productivity = ''
        for i in self.radioButtons4:
            if i.isChecked():
                productivity = i.text()

        note = self.textBox.toPlainText()

        poll = PollResult(self.opened, closed, activity, valence, arousal,dominance,productivity, note)
        self.app.writeToCSV(poll)
        self.app.updatePlot()
        self.hide()
        #self.app.writeToSpreadSheet(poll)


class QPlainTextEditSmall(QPlainTextEdit):
    def __init__(self, parent=None):
        QPlainTextEdit.__init__(self, parent)
    
    def sizeHint(self):
        return QSize(1,1)
    
    def minimumSizeHint(self):
        return QSize(1,1)

class PollResult:
    def __init__(self, opened, closed, activity, valence, arousal, dominance,productivity, note=''):
        self.opened = opened
        self.closed = closed        
        self.activity = activity
        self.valence = valence
        self.arousal = arousal
        self.dominance = dominance
        self.productivity = productivity
        self.note = note


