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