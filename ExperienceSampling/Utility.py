import os, sys, appdirs, platform, csv, socket, uuid, getpass, shutil
import numpy as np
from pathlib import Path
from urllib.request import urlopen
import datetime


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def isMSWindows():
    return os.name == 'nt' or platform.system() == 'Windows' or 'cygwin' in platform.system().lower()

def isMacOS():
    return platform.system() == 'Darwin'

def MSWindowsFix():
    if isMSWindows():
        import ctypes
        myappid = u'h3r0n.PersonalAnalytics.ExperienceSampling.1' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def MacOSFix():
    if isMacOS():
        import AppKit
        #NSApplicationActivationPolicyRegular = 0
        #NSApplicationActivationPolicyAccessory = 1
        #NSApplicationActivationPolicyProhibited = 2
        AppKit.NSApp.setActivationPolicy_(1)

def csvDirCheck():
    if not os.path.exists(csvDirPath()):
        os.makedirs(csvDirPath())

def csvFileCheck():
    return os.path.exists(csvFilePath())

def csvDirPath():
    return appdirs.user_data_dir('ExperienceSampling', 'UniBA')

def csvFilePath():
    return os.path.join(csvDirPath(), 'data.csv')

def csvDirRm():
    shutil.rmtree(appdirs.user_data_dir('ExperienceSampling', 'UniBA'), ignore_errors=True)

def exportPath():
    if os.name == 'nt' or platform.system() == 'Windows' or 'cygwin' in platform.system().lower():
        return os.path.join(os.path.join(str(Path.home()), "Desktop"),"data.csv")
    return os.path.join(str(Path.home()),'data.csv')

def csv2numpy(file, date=None):
        
    x = np.array([]).astype(int)
    y = np.array([]).astype(int)
    
    with open(file) as csv_file:      
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[6] == "POPUP_CLOSED":
                if date is None or date==datetime.datetime.fromtimestamp(int(row[0])).date():
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
        csvDirCheck()
        id = str(uuid.uuid4())
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

def nameSet():
    return os.path.exists(os.path.join(csvDirPath(), 'name'))

def setName(text):
    csvDirCheck()
    with open(os.path.join(csvDirPath(), 'name'), 'w') as file:
        file.write(text)

def getName():
    if nameSet():
        with open(os.path.join(csvDirPath(), 'name'), 'r') as file:
            return file.read()
    else:       
        setName(getLogin())
        
        return getLogin()

def getSheetName():
    return getName() + ":" + getID()

def earliestDate(file):
    with open(file) as csv_file:      
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[6] == "POPUP_CLOSED":
                date = row[0]
                return datetime.datetime.fromtimestamp(int(date)).date()
    raise ValueError

def todayDate():
    return datetime.date.today()

def pastDate(date, days):
    return date - datetime.timedelta(days=days)