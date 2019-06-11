import os, sys, appdirs, platform, csv
import numpy as np
from pathlib import Path

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