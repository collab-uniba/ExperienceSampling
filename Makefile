run:
	python ExperienceSampling.py

develop:
	pip install -r requirements.txt

build-windows:
	pyinstaller.exe --onefile --windowed --add-data "icons/*.png;icons" --icon "icons\icon.ico" --paths "C:\Windows\System32\downlevel" ExperienceSampling.py

build-linux:
	pyinstaller --onefile --windowed --add-data 'icons/*.png:icons' ExperienceSampling.py