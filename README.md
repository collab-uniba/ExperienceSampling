# ExperienceSampling

[Italian version](https://github.com/h3r0n/ExperienceSampling/blob/master/README_IT.md)

The goal of this project is to collect reports of affective experience with SAM (Self Assessment Manikin) methodology, in reaction to programming activities.

This application shows a notification every 60 minutes (by default). If the useres clicks on the notification, a form is displayed. The user can fill out the form by describing the emotions he experienced during the work day.

When the form is not displayed, the applications sits in the system tray waiting for the user or the next notification.

The data collected by the appplication is stored in a local database and can be exported at any time as a CSV file.

If the application is provided with a [credentials.json](https://gspread.readthedocs.io/en/latest/oauth2.html) file in the `data` folder, the database is synced with Google Spreadsheet. The spreadsheets are shared with the Google accounts listed in `data/sharelist.txt` (one email address per row).

The application allows the user to see a retrospective diagram based on Circumplex Model by James Russell. 

## Technology Used

- Python 3 (version not specified)
- Qt 5 (with pyqt package)

The application is **multi-platform** and it has been tested on Windows, Linux and Mac OS.
The icons come from this repository: https://github.com/collab-uniba/PersonalAnalytics/tree/field_study_merge

CSV file example:
```
1560297165,,,,,,POPUP_OPENED,
1560297173,Coding,3,4,5,Average,POPUP_CLOSED,
1560297178,,,,,,POPUP_OPENED,
1560297190,Taking a break,2,3,4,Under average,POPUP_CLOSED,I'm going to lunch.
1560297194,,,,,,POPUP_OPENED,
1560297219,Debugging,3,4,1,Average,POPUP_CLOSED,I can't fix a bug!
```

![Screenshot](screenshot.png)

# How to build a standalone executable

The dependencies list is contained in `requirements.txt` file. Install the dependencies with the `make develop` command.

To build a standalone executable for Linux, exec `make build` in a Linux environment to build an executable file called run.
To build a standalone executable for Windows exec `make build` in a Windows environment to build an .exe file .
To build a standalone executable for Mac OS esec `make build` in a Mac OS environment to build an .app file.

The executables will be located in the `dist` folder.

Before every new build, make sure to exec `make clean` to remove the `build` folder from previous builds.
