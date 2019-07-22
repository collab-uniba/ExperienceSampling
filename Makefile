ifeq ($(OS),Windows_NT)
	PYTHON = python
	PIP = pip
	PYINSTALLER = pyinstaller.exe
	BUILD_OPT = --onefile --windowed --add-data "data/*;data" --icon "data\icon.ico" --paths "C:\Windows\System32\downlevel"
	RM_FOLDER = rmdir /s /q
	DEPENDENCIES = -r requirements.txt
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		PYTHON = python3
		PIP = pip3
		PYINSTALLER = pyinstaller
		BUILD_OPT = --onefile --windowed --add-data 'data/*:data'
		RM_FOLDER = rm -R
		DEPENDENCIES = -r requirements.txt
	endif
	ifeq ($(UNAME_S),Darwin)
		PYTHON = python3
		PIP = pip3
		PYINSTALLER = pyinstaller
		BUILD_OPT = --onefile --windowed --add-data 'data/*:data' --icon "data/icon.icns"
		RM_FOLDER = rm -R
		DEPENDENCIES = -r requirements.txt
	endif
endif

run:
	$(PYTHON) run.py

debug:
	$(PYTHON) debug.py

develop:
	$(PIP) install $(DEPENDENCIES)

clean:
	$(RM_FOLDER) build

build:
	$(PYINSTALLER) $(BUILD_OPT) run.py
