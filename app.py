from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os

class MainWindow(QMainWindow):
    def __init__(self):
        # Be sure to call the super class method
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
        layout.addWidget(QComboBox(), 0, Qt.AlignHCenter)

        layout.addItem(QSpacerItem(25, 25, QSizePolicy.Minimum, QSizePolicy.Expanding))

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
            j.setPixmap(QPixmap(os.getcwd() + "/icons/V" + str(i) + ".png"))

        [feel1ImgLayout.addWidget(i, 0, Qt.AlignCenter) for i in images1]

        #radio buttons
        radioButtons1 = []
        [radioButtons1.append(QRadioButton(str(i))) for i in range(1,10)] 
        [feel1RadioLayout.addWidget(i) for i in radioButtons1]

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
            j.setPixmap(QPixmap(os.getcwd() + "/icons/A" + str(i) + ".png"))

        [feel2ImgLayout.addWidget(i, 0, Qt.AlignCenter) for i in images2]

        #radio buttons
        radioButtons2 = []
        [radioButtons2.append(QRadioButton(str(i))) for i in range(1,10)] 
        [feel2RadioLayout.addWidget(i) for i in radioButtons2]

        label2_1 = QLabel("Very calm")
        feel2LabelLayout.addWidget(label2_1)
        label2_2 = QLabel("Neutral")
        label2_2.setAlignment(Qt.AlignCenter)
        feel2LabelLayout.addWidget(label2_2)
        label2_3 = QLabel("Very excited")
        label2_3.setAlignment(Qt.AlignRight)
        feel2LabelLayout.addWidget(label2_3)

        layout.addItem(QSpacerItem(25, 25, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #notes
        label3 = QLabel('Notes (optional)')
        label3.setStyleSheet("font-size: 10pt; font-weight: bold;")
        layout.addWidget(label3)
        textBox = QPlainTextEdit()
        print(2*textBox.fontMetrics().lineSpacing())
        textBox.setFixedHeight(3*textBox.fontMetrics().lineSpacing())
        layout.addWidget(textBox)
        textBox.setPlaceholderText("Did you experience anything that might have affected your emotion during the last session?")

        layout.addItem(QSpacerItem(25, 25, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #footer
        doneLayout = QHBoxLayout()
        layout.addLayout(doneLayout)
        doneLayout.addWidget(QLabel())
        button1 = QPushButton("Done")
        doneLayout.addWidget(button1,0,Qt.AlignHCenter)
        label4 = QLabel("Export to csv...")
        label4.setAlignment(Qt.AlignRight)
        doneLayout.addWidget(label4)

        #tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(os.getcwd() + "/icons/status.png"))
        
        #tray logic
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

if __name__ == "__main__":
    import sys
 
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
