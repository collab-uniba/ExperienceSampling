from ExperienceSampling.App import App
import sys, os, appdirs
from PyQt5.QtWidgets import QApplication, QErrorMessage

lockfolder = appdirs.user_data_dir('ExperienceSampling', 'UniBA')
lockfile = os.path.join(lockfolder,'lockfile')

if not os.path.exists(lockfolder):
    os.makedirs(lockfolder)

try:
    if os.path.exists(lockfile):
        os.unlink(lockfile)
    fd =  os.open(lockfile, os.O_CREAT|os.O_EXCL|os.O_WRONLY)
except OSError as e:
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