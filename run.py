from ExperienceSampling.App import App
import sys, os, appdirs
from PyQt5.QtWidgets import QApplication, QErrorMessage
from lock import lock

lockfolder = appdirs.user_data_dir('ExperienceSampling', 'UniBA')
lockfile = os.path.join(lockfolder,'lockfile')

if not os.path.exists(lockfolder):
    os.makedirs(lockfolder)

if lock(lockfile):
    app = QApplication([])
    error_dialog = QErrorMessage()
    error_dialog.showMessage("Application already running!")
    sys.exit(app.exec_())

try:
    with open("timer.txt", 'r') as file:
        timer = file.read()
    timer = int(timer)
    app = App(pollTime=timer)
except (ValueError, FileNotFoundError):
    app = App()

sys.exit(app.exec_())