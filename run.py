from ExperienceSampling.App import App
import sys, os

try:
    with open("timer.txt", 'r') as file:
        timer = file.read()
    timer = int(timer)
    app = App(pollTime=timer)
except:
    app = App()

sys.exit(app.exec_())