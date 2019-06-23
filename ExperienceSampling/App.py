from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys, csv, shutil

from ExperienceSampling.Poll import Poll
from ExperienceSampling.Notification import Notification
from ExperienceSampling.Plot import Plot
from ExperienceSampling.Utility import *
from ExperienceSampling.SpreadSheetWriter import SpreadSheetWriterClass


class App(QApplication):

    def __init__(self, pollTime=60, postponeTime=60, debug=False):

        self.debug = debug

        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)   # HiDPI support
        MSWindowsFix()  # MS Windows taskbar fix

        # configure application
        QApplication.__init__(self, sys.argv)
        self.setQuitOnLastWindowClosed(False)
        self.setWindowIcon(QIcon(resource_path("data/taskbar.png")))
        MacOSFix()  # Hide dock icon in Mac OS

        # init timers
        self.pollTime = pollTime
        self.pollTimer = QTimer()
        self.pollTimerEnabled = True
        self.postponeTime = postponeTime
        self.postponeTimer = QTimer()

        # init windows
        self.notification = Notification(self)
        self.poll = Poll(self)
        self.plot = Plot(self)

        # set timer actions
        self.pollTimer.timeout.connect(self.notification.show)
        self.postponeTimer.timeout.connect(self.notification.show)

        if checkCredentials() and not nameSet():
            self.inputName(self.notification)

        self.startPollTimer()

        if checkCredentials():
            self.spreadSheetWriter = SpreadSheetWriterClass()

    def inputName(self, window):
            text, okPressed = QInputDialog.getText(window, "Who are you?", "Insert your name and surname:", QLineEdit.Normal, "")
            
            if okPressed and text != '':
                setName(text)
            else:
                setName(getLogin)

    def minutes(self):
        if self.debug==True:
            return 1
        return 60

    def setPollTimer(self,value):
        self.pollTime = value
        self.stopPollTimer()
        self.startPollTimer()

    def startPollTimer(self):
        if self.pollTimerEnabled and self.pollTime>0:
            self.pollTimer.start(self.pollTime*1000*self.minutes())

    def stopPollTimer(self):
        self.pollTimer.stop()

    def setPostponeTimer(self,value):
        self.postponeTime = value

    def startPostponeTimer(self):
        self.postponeTimer.start(self.postponeTime*1000*self.minutes())
    
    def stopPostponeTimer(self):
        self.postponeTimer.stop()

    def showPoll(self):

        self.poll.show()

    def showPlot(self):
        self.plot.show()

    def writeToCSV(self, poll):
        csvDirCheck()
        with open(csvFilePath(), mode='a', newline='') as data:
            data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow([poll.opened,'','','','','','POPUP_OPENED',''])
            data_writer.writerow([poll.closed,poll.activity,poll.valence,poll.arousal,poll.dominance,poll.productivity,'POPUP_CLOSED',poll.note])

    def writeToSpreadSheet(self,poll):
        if checkCredentials():
            self.spreadSheetWriter.writeOnsheet([poll.opened, '', '', '', '','','POPUP_OPENED', ''])
            self.spreadSheetWriter.writeOnsheet([poll.closed,poll.activity,poll.valence,poll.arousal,poll.dominance,poll.productivity,'POPUP_CLOSED',poll.note])


    def exportCSV(self):
        if csvFileCheck():
            name = QFileDialog.getSaveFileName(caption='Salva dati', directory=exportPath(), filter='CSV(*.csv)')
            if name[0]:      
                shutil.copyfile(csvFilePath(), name[0])
        else:
            msg = QMessageBox()
            msg.setText("Cannot export to csv")
            msg.setInformativeText("The database is still empty. Please take the poll at least once.")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            

    def updatePlot(self):
        self.plot.mpl.update_figure()
