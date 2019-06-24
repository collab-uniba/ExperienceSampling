# ExperienceSampling

The project is done to analyze emotions with SAM (Self Assessment Manikin) methodology.

This application show a notification every 60 minutes (by default). 
Clicking the notification is displayed a form, which a user fill with him emotion in that time slice, in a work day.
Filled the form, the application work in background and is visible in the system tray.

The data are saved on a local CSV file with timestamp log (window opening/closing time).
If the app is compiled with file  [credentials.json](https://gspread.readthedocs.io/en/latest/oauth2.html) located in `data` folder, 
the data saved are uploaded to a Google Spreadheets file. To be able to see the data is necessary share a spreadsheet with google account,
to do that is necessary insert a list of mail account in a file called sharelist.txt located in  `data/sharelist.txt`, one mail each row.

The application allow you to see a retrospective diagram based on Circumplex Model by James Russell. 

## Technology Used

- Python 3 (version not specified)
- Qt 5 (with pyqt package)

The application is **multi-platform**, it is tested on Windows and Linux.
The icons came from this repository https://github.com/collab-uniba/PersonalAnalytics/tree/field_study_merge

Esempio di file csv:
```
1560297165,,,,,,POPUP_OPENED,
1560297173,Coding,3,4,5,average,POPUP_CLOSED,
1560297178,,,,,,POPUP_OPENED,
1560297190,Taking a break,2,3,4,under average,POPUP_CLOSED,I'm going to lunch.
1560297194,,,,,,POPUP_OPENED,
1560297219,Debugging,3,4,1,average,POPUP_CLOSED,I can't fix a bug!
```

![Screenshot](screenshot.png)

# How to generate an executable
The dependencies list is contained in `requirements.txt` file.
Is possible install the dependencies with the `make develop` command.

To generate a standalone executable for Linux, exec `make build` to generate an executable file called run.
To generate a standalone executable for Windows exec `make build` to generate an .exe file .
To generate a standalone executable for Mac OS esec `make build` to generate an .app file.

The executable if the generation is ok are save in the `dist` folder.
Before every build exec `make clean` to remove the `build` folder.
