run:
	python ExperienceSampling.py

develop:
	pip install -r requirements.txt

build-windows:
	pyinstaller.exe --onefile --windowed --add-data "data/*;data" --icon "data\icon.ico" --paths "C:\Windows\System32\downlevel" ExperienceSampling.py

build-linux:
	pyinstaller --onefile --windowed --add-data 'data/*:data' ExperienceSampling.py