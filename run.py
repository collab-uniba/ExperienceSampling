""""""

from ExperienceSampling.App import App
import sys, os, appdirs
from PyQt5.QtWidgets import QApplication, QErrorMessage
from lock import lock

lockfolder = appdirs.user_data_dir('ExperienceSampling', 'UniBA')
lockfile = os.path.join(lockfolder,'lockfile')

if not os.path.exists(lockfolder):
    os.makedirs(lockfolder)

# display an error if other instances are running
if lock(lockfile):
    app = QApplication([])
    error_dialog = QErrorMessage()
    error_dialog.showMessage("Application already running!")
    sys.exit(app.exec_())

try:
    # the content of "timer.txt" defines the default timer
    with open("timer.txt", 'r') as file:
        timer = file.read()
    timer = int(timer)
    app = App(pollTime=timer)
except (ValueError, FileNotFoundError):
    # if "timer.txt" is not present, the default timer is set to 60'
    app = App()

sys.exit(app.exec_())
