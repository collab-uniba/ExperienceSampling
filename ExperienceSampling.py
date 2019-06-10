#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os, sys, time, csv, datetime, shutil, platform, appdirs

from MainWindow import *

if __name__ == "__main__":

    if os.name == 'nt' or platform.system() == 'Windows' or 'cygwin' in platform.system().lower():
        import ctypes
        myappid = u'h3r0n.PersonalAnalytics.ExperienceSampling.1' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setWindowIcon(QIcon(resource_path("icons/status.png")))
    mw = MainWindow(60)
    mw.show()

    sys.exit(app.exec_())

