run:
	python run.py

debug:
	python debug.py

develop:
	pip install -r requirements.txt

build-windows:
	pyinstaller.exe --onefile --windowed --add-data "data/*;data" --icon "data\icon.ico" --paths "C:\Windows\System32\downlevel" run.py
	ren dist\run.exe ExperienceSampling.exe

build-linux:
	pyinstaller --onefile --windowed --add-data 'data/*:data' run.py
	mv dist/run dist/ExperienceSampling
