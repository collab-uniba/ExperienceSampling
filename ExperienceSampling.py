#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#import os, sys, time, csv, datetime, shutil, platform, appdirs
import sys, csv, shutil

from Poll import Poll
from Notification import Notification
from Plot import Plot
from Utility import *
from SpreadSheetWriter import SpreadSheetWriterClass

class ExperienceSampling(QApplication):

    def __init__(self, pollTime=60, postponeTime=60, debug=False):

        self.debug = debug

        self.spreadSheetWriter = SpreadSheetWriterClass()

        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)   # HiDPI support
        MSWindowsFix()  # MS Windows taskbar fix

        # configure application
        QApplication.__init__(self, sys.argv)
        self.setQuitOnLastWindowClosed(False)
        self.setWindowIcon(QIcon(resource_path("icons/taskbar.png")))

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

        self.startPollTimer()

        # debug
        #print(homePath())
        #self.poll.show()
        #self.notification.show()

    def minutes(self):
        if self.debug==True:
            return 1
        return 60

    def setPollTimer(self,value):
        self.pollTime = value

    def startPollTimer(self):
        if self.pollTimerEnabled and self.pollTime>0:
            self.pollTimer.start(self.pollTime*1000*self.minutes())

    def stopPollTimer(self):
        self.pollTimer.stop()

    def setPostponeTimer(self,value):
        self.postponeTime = value

    def startPostponeTimer(self):
        self.postponeTimer.start(self.postponeTime*1000*self.minutes())

    def showPoll(self):
        self.poll.show()

    def showPlot(self):
        self.plot.show()

    def writeToCSV(self, poll):
        csvDirCheck()
        with open(csvFilePath(), mode='a', newline='') as data:
            data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow([poll.opened,'','','','POPUP_OPENED',''])
            data_writer.writerow([poll.closed,poll.activity,poll.valence,poll.arousal,'POPUP_CLOSED',poll.note])

    def writeToSpreadSheet(self,poll):
        self.spreadSheetWriter.writeOnsheet([poll.opened, '', '', '', 'POPUP_OPENED', ''])
        self.spreadSheetWriter.writeOnsheet([poll.closed,poll.activity,poll.valence,poll.arousal,'POPUP_CLOSED',poll.note])


    def exportCSV(self):
        name = QFileDialog.getSaveFileName(caption='Salva dati', directory=exportPath(), filter='CSV(*.csv)')
        if name[0]:      
            shutil.copyfile(self.filepath, name[0])

if __name__ == "__main__":

    app = ExperienceSampling(pollTime=1, debug=True)
    sys.exit(app.exec_())

