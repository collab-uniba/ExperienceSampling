import os, sys, appdirs, platform, csv, socket, uuid, getpass
import numpy as np
from pathlib import Path
from urllib.request import urlopen


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def MSWindowsFix():
    if os.name == 'nt' or platform.system() == 'Windows' or 'cygwin' in platform.system().lower():
        import ctypes
        myappid = u'h3r0n.PersonalAnalytics.ExperienceSampling.1' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def csvDirCheck():
    if not os.path.exists(csvDirPath()):
        os.makedirs(csvDirPath())

def csvFileCheck():
    return os.path.exists(csvFilePath())

def csvDirPath():
    return appdirs.user_data_dir('ExperienceSampling', 'UniBA')

def csvFilePath():
    return os.path.join(csvDirPath(), 'data.csv')

def exportPath():
    if os.name == 'nt' or platform.system() == 'Windows' or 'cygwin' in platform.system().lower():
        return os.path.join(os.path.join(str(Path.home()), "Desktop"),"data.csv")
    return os.path.join(str(Path.home()),'data.csv')

def csv2numpy(file):
        
    x = np.array([]).astype(int)
    y = np.array([]).astype(int)
    
    with open(file) as csv_file:      
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[4] == "POPUP_CLOSED":
                x = np.append(x,int(row[2]))
                y = np.append(y,int(row[3]))

    return (x,y)

def internet_on():
    try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
    except:
        return False

def getLogin():
    return getpass.getuser() + "@" + socket.gethostname()

def getID():
    """ Returns an unique user/machine identifier """
    if os.path.exists(os.path.join(csvDirPath(), 'id')):
        with open(os.path.join(csvDirPath(), 'id'), 'r') as file:
            return file.read()
    else:
        id = getLogin() + ":" + str(uuid.uuid4())
        with open(os.path.join(csvDirPath(), 'id'), 'w') as file:
            file.write(id)
        return id

def toCommitPath():
    return os.path.join(csvDirPath(), 'toCommit.csv')

def toCommitCheck():
    return os.path.exists(toCommitPath())

def checkCredentials():
    return os.path.exists(resource_path('data/credentials.json'))

def checkSharelist():
    return os.path.exists(resource_path('data/sharelist.txt'))

def sharelist():
    with open(resource_path('data/sharelist.txt'), 'r') as f:
        x = f.read().splitlines()
    return x