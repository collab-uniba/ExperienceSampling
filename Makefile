ifeq ($(OS),Windows_NT)
	PYTHON = python
	PIP = pip
	PYINSTALLER = pyinstaller.exe
	BUILD_OPT = --onefile --windowed --add-data "data/*;data" --icon "data\icon.ico" --paths "C:\Windows\System32\downlevel"
	RM_FOLDER = rmdir /s /q
else
	PYTHON = python3
	PIP = pip3
	PYINSTALLER = pyinstaller
	BUILD_OPT = --onefile --windowed --add-data 'data/*:data'
	RM_FOLDER = rm -R
endif

run:
	$(PYTHON) run.py

debug:
	$(PYTHON) debug.py

develop:
	$(PIP) install -r requirements.txt

clean:
	$(RM_FOLDER) build

build:
	$(PYINSTALLER) $(BUILD_OPT) run.py
