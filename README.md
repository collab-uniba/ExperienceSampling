# ExperienceSampling

The goal of this project is to collect reports of affective experience with SAM (Self Assessment Manikin) methodology, in reaction to programming activities.

This application shows a notification every 60 minutes (by default). If the useres clicks on the notification, a form is displayed. The user can fill out the form by describing the emotions he experienced during the work day.

When the form is not displayed, the applications sits in the system tray waiting for the user or the next notification.

The data collected by the appplication is stored in a local database and can be exported at any time as a CSV file.

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

![Screenshot](screenshots/screenshot.png)

# User manual

Run the executable to open the application. ExperienceSampling is a portable app and requires no installation.

![](screenshots/icon.png)

Every 60 minutes (default timer) a notification will appear.

![](screenshots/notification.png)

The default timer can be defined by placing a file named `timer.txt` in the executable folder. `timer.txt` should only contain a single line representing the number of minutes.

Once the notification appears, you have tree options:
 - Dismiss: the timer is disabled. You have to re-enable it from the tray menu
 - Postpone: the notification will appear later again. Use the slider to decide when.
![](screenshots/postpone.png)
 - Open the popup: click anywhere on the notification to open the following popup window

![](screenshots/popup.png)

Note: all fields except "Notes" aren't optional. After filling in the form, press the "Done" button to submit. Your data is stored in a local database and can be exported at any time from the tray menu.

![](screenshots/export.png)

After you close the popup window by pressing done, the timer (if not disabled) will again and the notification will appear again after the set amount of time.

Select "Show retrospective" from the tray menu to show a visual representation of your data as a bubble chart, according to the [Russel Circumplex Model](https://s3.amazonaws.com/academia.edu.documents/38425675/Russell1980.pdf?response-content-disposition=inline%3B%20filename%3DRussell1980.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWOWYYGZ2Y53UL3A%2F20190626%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190626T124820Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=1213c8343f13b65494a57cc0cc31a3ec75d3332f1358e9c102ced93e032e3850).

![](screenshots/retrospective_all.png)

Check "View single day" and move the slider to filter your emotions by day.

![](screenshots/retrospective_day.png)



# How to build a standalone executable

The dependencies list is contained in `requirements.txt` file. Install the dependencies with the `make develop` command.

To build a standalone executable for Linux, exec `make build` in a Linux environment to build an executable file called run.
To build a standalone executable for Windows exec `make build` in a Windows environment to build an .exe file .
To build a standalone executable for Mac OS esec `make build` in a Mac OS environment to build an .app file.

The executables will be located in the `dist` folder.

Before every new build, make sure to exec `make clean` to remove the `build` folder from previous builds.
