from ExperienceSampling.App import App
import sys, os, appdirs

lockfolder = appdirs.user_data_dir('ExperienceSampling', 'UniBA')
lockfile = os.path.join(lockfolder,'lockfile')

if not os.path.exists(lockfolder):
    os.makedirs(lockfolder)

try:
    if os.path.exists(lockfile):
        os.unlink(lockfile)

    fd =  os.open(lockfile, os.O_CREAT|os.O_EXCL|os.O_RDWR)

    with open("timer.txt", 'r') as file:
        timer = file.read()
    timer = int(timer)
    app = App(pollTime=timer)
except OSError:
    raise "Application already running."
except (ValueError, FileNotFoundError):
    app = App()

sys.exit(app.exec_())